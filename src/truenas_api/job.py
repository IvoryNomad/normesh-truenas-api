import logging
from typing import Any, Dict, List, Optional, Union

from .connection import TrueNASConnection, TrueNASResponse

logger = logging.getLogger(__name__)


class JobManager:
    """Manages TrueNAS job operations.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    core.get_jobs (as query, get_intance)               |     Yes     |  0.1.0  | No
    core.job_abort                                      |     No      |         | No
    core.download_jobs                                  |     No      |         | No
    core.job_wait                                       |     No      |         | Yes

    Jobs represent long-running operations in TrueNAS. This manager provides methods to:
    - Query job status
    - Wait for job completion (local method)
    - Get job results

    A job response contains:
    - id: Unique job identifier
    - method: API method that created the job
    - state: Current state (WAITING, RUNNING, SUCCESS, FAILED, ABORTED)
    - progress: Dict with percent complete and description
    - result: Final result data if complete
    - error: Error message if failed
    - time_started: When job started
    - time_finished: When job completed
    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize job manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection

    async def query(
        self, filters: Optional[List] = None, options: Optional[Dict] = None
    ) -> Union[List[Dict], Dict, int]:
        """Query jobs based on filters and options.

        Args:
            filters: List of filters (e.g. [["id", "=", 123]])
            options: Query options including:
                - count: Return count of matching jobs
                - extend: Include additional data
                - extra: Additional parameters
                - get: Return single object
                - limit/offset: Pagination
                - select: Fields to return
                - force_sql_filters: Force SQL filtering

        Returns:
            List of matching jobs, single job dict, or count depending on options

        Raises:
            JobError: If query fails
        """
        params = []
        if filters:
            params.append(filters)
        if options:
            params.append(options)

        logger.debug("Querying jobs with params: %s", params)
        response = await self.conn._call("core.get_jobs", params)

        if response.error:
            logger.error("Failed to query jobs: %s", response.error)
            raise JobError(f"Failed to query jobs: {response.error}")

        return response.result

    async def get_instance(
        self, job_id: int, include_progress: bool = True
    ) -> Dict[str, Any]:
        """Get details about a specific job.

        Args:
            job_id: ID of job to query
            include_progress: Include progress info

        Returns:
            Dict containing job information

        Raises:
            JobError: If job not found or query fails
        """
        logger.debug("Getting job instance %d", job_id)

        options = {"extra": {"include_progress": include_progress}}

        jobs = await self.query(filters=[["id", "=", job_id]], options=options)

        if not jobs:
            logger.error("Job %d not found", job_id)
            raise JobError(f"Job {job_id} not found")

        return jobs[0]

    async def wait(
        self,
        job_id: int,
        timeout: Optional[int] = None,
        interval: int = 2,
        raise_error: bool = True,
    ) -> Dict[str, Any]:
        """Wait for a job to complete.

        Args:
            job_id: ID of job to wait for
            timeout: Maximum seconds to wait (None for no timeout)
            interval: Seconds between status checks
            raise_error: Raise exception if job fails

        Returns:
            Final job status

        Raises:
            JobError: If job fails and raise_error is True
            TimeoutError: If timeout is reached
        """
        import asyncio
        from datetime import datetime, timedelta

        logger.debug(
            "Waiting for job %d (timeout=%s, interval=%d)", job_id, timeout, interval
        )

        start_time = datetime.now()
        while True:
            status = await self.get_instance(job_id)

            if status["state"] in ["SUCCESS", "FAILED", "ABORTED"]:
                if status["state"] == "SUCCESS" or not raise_error:
                    logger.info(
                        "Job %d completed with state %s", job_id, status["state"]
                    )
                    return status
                else:
                    error = status.get("error") or "Unknown error"
                    logger.error("Job %d failed: %s", job_id, error)
                    raise JobError(f"Job failed: {error}")

            if timeout:
                elapsed = (datetime.now() - start_time).total_seconds()
                if elapsed > timeout:
                    logger.error("Timeout waiting for job %d", job_id)
                    raise TimeoutError(f"Timeout waiting for job {job_id}")

            await asyncio.sleep(interval)


class JobError(Exception):
    """Raised when a job operation fails."""

    pass
