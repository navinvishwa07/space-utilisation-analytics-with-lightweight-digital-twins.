"""
Build this system using production-grade engineering standards.
Use clean architecture with strict separation of concerns.
Write modular, testable, maintainable code designed for long-term scaling.
Avoid hardcoded values. Use configuration management.
Include structured logging, validation, and defensive error handling.
Document why decisions are made, not just what is implemented.
Assume this will undergo senior engineering review.
Optimize for clarity, reliability, observability, and extensibility over speed.
"""

from backend.repository.data_repository import (
    initialize_database,
    seed_synthetic_data,
)


def startup():
    initialize_database()
    seed_synthetic_data()
    print("System ready.")


if __name__ == "__main__":
    startup()