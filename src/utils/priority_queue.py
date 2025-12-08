"""
Priority Queue for ETL job scheduling.
Chapter 1: Data Structures

YOUR TASK: Implement priority queue for scheduling ETL jobs
"""

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
    
    TODO: Understand @dataclass decorator:
    - What does order=True do?
    - What does field(compare=True/False) mean?
    - Why do we need default_factory?
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
        """
        Initialize job scheduler.
        
        TODO: Initialize:
        - self._heap (empty list for heapq)
        - self._counter (for tie-breaking)
        - self._jobs_completed (track completed jobs)
        """
        pass
    
    def schedule_job(self, job_id: str, job_type: str, 
                    priority: JobPriority = JobPriority.NORMAL,
                    config: dict = None) -> None:
        """
        Schedule a new ETL job.
        
        Args:
            job_id: Unique job identifier
            job_type: Type of job ('extract', 'transform', 'load')
            priority: Job priority level
            config: Job configuration dict
        
        TODO:
        1. Create ETLJob object
        2. Push to heap as tuple (priority, counter, job)
        3. Increment counter
        
        Hint: Use heapq.heappush()
        """
        pass
    
    def get_next_job(self) -> Optional[ETLJob]:
        """
        Get next highest priority job.
        
        Returns:
            ETLJob or None if queue is empty
        
        TODO:
        1. Check if heap is empty
        2. Pop from heap using heapq.heappop()
        3. Extract job from tuple
        4. Return job
        """
        pass
    
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
