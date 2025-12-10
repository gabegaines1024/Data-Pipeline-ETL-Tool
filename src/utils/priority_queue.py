import heapq
from dataclasses import dataclass, field
from typing import Any, Optional
from datetime import datetime
from enum import IntEnum


class JobPriority(IntEnum):
    """Job priority levels (lower number = higher priority)."""
    CRITICAL = 1
    HIGH = 2
    NORMAL = 3
    LOW = 4
    BACKGROUND = 5


@dataclass(order=True)
class ETLJob:
    """
    Represents an ETL job with priority and metadata.
    """
    priority: int = field(compare=True)
    created_at: datetime = field(compare=True, default_factory=datetime.now)
    job_id: str = field(compare=False)
    job_type: str = field(compare=False)  # 'extract', 'transform', 'load'
    config: dict = field(compare=False, default_factory=dict)
    
    def __repr__(self):
        return f"ETLJob(id={self.job_id}, type={self.job_type}, priority={self.priority})"

class JobScheduler:
    """Priority-based job scheduler for ETL pipeline."""
    
    def __init__(self):
        self._queue = []
        self._counter = 0
        self._jobs_completed = 0
    
    def schedule_job(self, job_id: str, job_type: str, 
                    priority: JobPriority = JobPriority.NORMAL,
                    config: dict = None) -> None:
        """
        Schedule a new ETL job.
        """
        #ETL Job object:
        etl_job = ETLJob(JobPriority, job_id, job_type)

        #Push to heap as a tuple
        heaqp.heappush(self._queue, etl_job)
        
        #increment counter
        self._counter += 1
    
    def get_next_job(self) -> Optional[ETLJob]:
        """
        Get next highest priority job.
        """

        #check if the queue is empty
        if !(self._queue):
            return None
        
        #get the job tuple
        job_info = self._queue.heapq.heappop()
        
        #get the job id
        job = job_info.job_id

        #return the job id
        return job
    
    def peek_next(self) -> Optional[ETLJob]:
        """
        View next job without removing it.
        
        TODO:
        1. Check if heap is empty
        2. Look at heap[0]
        3. Extract job from tuple
        4. Return job (don't pop!)
        """
        pass
    
    def is_empty(self) -> bool:
        """Check if scheduler has pending jobs."""
        # TODO: Return whether heap is empty
        pass
    
    def pending_jobs(self) -> int:
        """Return number of pending jobs."""
        # TODO: Return length of heap
        pass
    
    def complete_job(self, job: ETLJob) -> None:
        """Mark job as completed (for tracking)."""
        # TODO: Increment completed counter
        pass
    
    def stats(self) -> dict:
        """
        Return scheduler statistics.
        
        TODO: Return dict with:
        - pending: number of pending jobs
        - completed: number of completed jobs
        - next_priority: priority of next job (or None)
        """
        pass
    
    def __len__(self):
        """Return number of pending jobs."""
        # TODO: Return heap length
        pass
    
    def __repr__(self):
        """String representation."""
        # TODO: Return informative string
        pass


class DependencyResolver:
    """
    Resolves job dependencies for complex ETL workflows.
    
    BONUS CHALLENGE: Implement this after basic scheduler works
    
    Example:
    - Job C depends on Job A and Job B completing first
    - Schedule jobs in correct order
    """
    
    def __init__(self, scheduler: JobScheduler):
        """
        Initialize dependency resolver.
        
        TODO:
        - Store scheduler reference
        - Track dependencies (dict of job_id -> list of dependencies)
        - Track completed jobs
        """
        pass
    
    def add_dependency(self, job_id: str, depends_on: list[str]) -> None:
        """
        Add job dependency.
        
        Args:
            job_id: Job that has dependencies
            depends_on: List of job IDs that must complete first
        
        TODO: Store in dependencies dict
        """
        pass
    
    def can_schedule(self, job_id: str) -> bool:
        """
        Check if job's dependencies are satisfied.
        
        TODO:
        1. Get dependencies for job
        2. Check if all dependencies are in completed set
        3. Return True if can schedule, False otherwise
        """
        pass
    
    def schedule_with_dependencies(self, job_id: str, job_type: str,
                                   priority: JobPriority,
                                   depends_on: list[str] = None) -> None:
        """
        Schedule job if dependencies are met.
        
        TODO:
        1. Add dependencies if provided
        2. Check if can schedule
        3. If yes, schedule with scheduler
        4. If no, add to waiting queue
        """
        pass
