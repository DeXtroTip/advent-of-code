__all__ = [
  'timer',
  'Timer',
  'TimerError',
]
import time


class TimerError(Exception):
  """A custom exception used to report errors in use of Timer class"""


class Timer:

  def __init__(self, log_text="Elapsed time: {:0.5f} s"):
    self.log_text = log_text
    self._start_time = None
    self._elapsed_time = None

  def start(self, force=True) -> None:
    """Start a new timer"""
    if self._start_time is not None and not force:
      raise TimerError("Timer is running. Use .stop() to stop it")

    self._start_time = time.perf_counter()
    self._elapsed_time = 0

  def stop(self, log=False) -> float:
    """Stop the timer, and report the elapsed time"""
    if self._start_time is None:
      raise TimerError("Timer is not running. Use .start() to start it")

    self._elapsed_time = time.perf_counter() - self._start_time
    self._start_time = None

    if log:
      self.log()

    return self._elapsed_time

  def lap(self, log=False) -> float:
    """Lap the timer, stop current one and restart, and report the elapsed time"""
    elapsed_time = self.stop(log)
    self.start()
    return elapsed_time

  def log(self) -> None:
    print(self.log_text.format(self._elapsed_time))  # noqa: T201


timer = Timer()
