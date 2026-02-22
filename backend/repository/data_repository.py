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

import sqlite3
import os
import random
from datetime import datetime, timedelta


# -----------------------------
# Database Path
# -----------------------------
def get_database_path() -> str:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    return os.path.join(data_dir, "siet.db")


# -----------------------------
# Schema Initialization
# -----------------------------
def initialize_database() -> None:
    db_path = get_database_path()

    try:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            capacity INTEGER NOT NULL CHECK (capacity > 0),
            room_type TEXT NOT NULL,
            location TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS BookingHistory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            time_slot TEXT NOT NULL,
            occupied INTEGER NOT NULL CHECK (occupied IN (0,1)),
            FOREIGN KEY (room_id) REFERENCES Rooms(id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            requested_capacity INTEGER NOT NULL CHECK (requested_capacity > 0),
            requested_date TEXT NOT NULL,
            requested_time_slot TEXT NOT NULL,
            priority_weight REAL NOT NULL DEFAULT 1.0,
            status TEXT NOT NULL DEFAULT 'PENDING'
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS AllocationLogs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            request_id INTEGER NOT NULL,
            room_id INTEGER NOT NULL,
            allocation_score REAL,
            allocated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (request_id) REFERENCES Requests(id),
            FOREIGN KEY (room_id) REFERENCES Rooms(id)
        );
        """)

        conn.commit()
        conn.close()

    except Exception as e:
        raise RuntimeError(f"Database initialization failed: {e}")


# -----------------------------
# Synthetic Data Seeding
# -----------------------------
def seed_synthetic_data() -> None:
    db_path = get_database_path()

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM Rooms;")
        room_count = cursor.fetchone()[0]

        if room_count > 0:
            print("Synthetic data already exists. Skipping seeding.")
            conn.close()
            return

        rooms = [
            ("Room A", 30, "Classroom", "Block 1"),
            ("Room B", 50, "Auditorium", "Block 1"),
            ("Room C", 20, "Lab", "Block 2"),
            ("Room D", 40, "Classroom", "Block 2"),
            ("Room E", 25, "Seminar", "Block 3"),
            ("Room F", 60, "Auditorium", "Block 3"),
            ("Room G", 35, "Classroom", "Block 4"),
            ("Room H", 45, "Lab", "Block 4"),
            ("Room I", 30, "Seminar", "Block 5"),
            ("Room J", 55, "Auditorium", "Block 5"),
        ]

        cursor.executemany("""
            INSERT INTO Rooms (name, capacity, room_type, location)
            VALUES (?, ?, ?, ?);
        """, rooms)

        conn.commit()

        time_slots = ["09-11", "11-13", "14-16", "16-18"]
        start_date = datetime.today() - timedelta(days=21)

        cursor.execute("SELECT id FROM Rooms;")
        room_ids = [row[0] for row in cursor.fetchall()]

        booking_entries = []

        for day in range(21):
            current_date = (start_date + timedelta(days=day)).strftime("%Y-%m-%d")
            weekday = (start_date + timedelta(days=day)).weekday()

            for room_id in room_ids:
                for slot in time_slots:
                    if weekday < 5:
                        occupied = 1 if random.random() < 0.65 else 0
                    else:
                        occupied = 1 if random.random() < 0.35 else 0

                    booking_entries.append(
                        (room_id, current_date, slot, occupied)
                    )

        cursor.executemany("""
            INSERT INTO BookingHistory (room_id, date, time_slot, occupied)
            VALUES (?, ?, ?, ?);
        """, booking_entries)

        conn.commit()
        conn.close()

        print("Synthetic data seeded successfully.")

    except Exception as e:
        raise RuntimeError(f"Synthetic data seeding failed: {e}")