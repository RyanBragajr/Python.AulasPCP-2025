import math
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class Location:
    latitude: float
    longitude: float

@dataclass
class Reporter:
    full_name: str
    document_id: str
    email: str
    phone: str
    location: Location

@dataclass
class Report:
    reporter: Reporter
    disaster_type: str
    description: str
    date: datetime
    location: Location

class DisasterReportCLI:
    def __init__(self):
        # Default reference point (latitude, longitude) - can be changed by user
        self.reference_point = Location(latitude=0.0, longitude=0.0)
        self.reports: List[Report] = []

    @staticmethod
    def haversine_distance(loc1: Location, loc2: Location) -> float:
        # Calculate the great-circle distance between two points on the Earth surface.
        R = 6371.0  # Earth radius in kilometers
        lat1_rad = math.radians(loc1.latitude)
        lat2_rad = math.radians(loc2.latitude)
        delta_lat = math.radians(loc2.latitude - loc1.latitude)
        delta_lon = math.radians(loc2.longitude - loc1.longitude)

        a = math.sin(delta_lat / 2)**2 + \
            math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = R * c
        return distance

    def is_within_radius(self, loc: Location, radius_km=10.0) -> bool:
        distance = self.haversine_distance(self.reference_point, loc)
        return distance <= radius_km

    def input_location(self, prompt_prefix="") -> Optional[Location]:
        try:
            lat_str = input(f"{prompt_prefix}Latitude (decimal degrees): ").strip()
            lon_str = input(f"{prompt_prefix}Longitude (decimal degrees): ").strip()
            latitude = float(lat_str)
            longitude = float(lon_str)
            if not (-90 <= latitude <= 90 and -180 <= longitude <= 180):
                print("Invalid latitude or longitude values.")
                return None
            return Location(latitude, longitude)
        except ValueError:
            print("Invalid input for latitude or longitude.")
            return None

    def input_date_time(self) -> Optional[datetime]:
        try:
            date_str = input("Date (YYYY-MM-DD): ").strip()
            time_str = input("Time (HH:MM, 24h format): ").strip()
            dt_str = f"{date_str} {time_str}"
            dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
            return dt
        except ValueError:
            print("Invalid date or time format.")
            return None

    def add_report(self):
        print("\nEnter reporter information:")
        full_name = input("Full name: ").strip()
        document_id = input("Document ID: ").strip()
        email = input("Email: ").strip()
        phone = input("Phone: ").strip()
        print("Reporter location:")
        reporter_location = self.input_location("  ")
        if reporter_location is None:
            print("Failed to input valid reporter location. Report creation aborted.")
            return

        reporter = Reporter(
            full_name=full_name,
            document_id=document_id,
            email=email,
            phone=phone,
            location=reporter_location
        )

        print("\nEnter disaster report details:")
        disaster_type = input("Type of disaster (e.g., flood, fire, landslide): ").strip().lower()
        description = input("Description: ").strip()
        dt = self.input_date_time()
        if dt is None:
            print("Failed to input valid date/time. Report creation aborted.")
            return
        print("Report location:")
        report_location = self.input_location("  ")
        if report_location is None:
            print("Failed to input valid report location. Report creation aborted.")
            return

        if not self.is_within_radius(report_location):
            print(f"Report location is NOT within 10 km radius from the reference point.")
            return
        else:
            print("Report location validated within 10 km radius.")

        report = Report(
            reporter=reporter,
            disaster_type=disaster_type,
            description=description,
            date=dt,
            location=report_location
        )
        self.reports.append(report)
        print("Report successfully added!")

    def list_reports(self, filtered_reports: Optional[List[Report]] = None):
        reports_to_show = filtered_reports if filtered_reports is not None else self.reports
        if not reports_to_show:
            print("\nNo reports found.")
            return

        print(f"\nListing {len(reports_to_show)} report(s):")
        for i, r in enumerate(reports_to_show, start=1):
            print(f"\nReport #{i}:")
            print(f"  Reporter: {r.reporter.full_name} (Document: {r.reporter.document_id})")
            print(f"  Contact: Email: {r.reporter.email}, Phone: {r.reporter.phone}")
            print(f"  Reporter Location: ({r.reporter.location.latitude}, {r.reporter.location.longitude})")
            print(f"  Disaster Type: {r.disaster_type.capitalize()}")
            print(f"  Description: {r.description}")
            print(f"  Date & Time: {r.date.strftime('%Y-%m-%d %H:%M')}")
            print(f"  Report Location: ({r.location.latitude}, {r.location.longitude})")
            dist = self.haversine_distance(self.reference_point, r.location)
            print(f"  Distance from reference: {dist:.2f} km")

    def search_reports(self):
        print("\nSearch reports by:")
        print("1 - Disaster type")
        print("2 - Location radius")
        print("3 - Date period")
        choice = input("Choose option (1-3): ").strip()
        if choice == "1":
            typ = input("Enter disaster type to search (case insensitive): ").strip().lower()
            filtered = [r for r in self.reports if r.disaster_type == typ]
            self.list_reports(filtered)
        elif choice == "2":
            loc = self.input_location("Search center ")
            if loc is None:
                print("Invalid location. Search aborted.")
                return
            try:
                radius_str = input("Enter radius in km (max 10 km): ").strip()
                radius = float(radius_str)
                if not (0 < radius <= 10):
                    print("Radius must be between 0 and 10 km.")
                    return
            except ValueError:
                print("Invalid radius value.")
                return
            filtered = [r for r in self.reports if self.haversine_distance(loc, r.location) <= radius]
            self.list_reports(filtered)
        elif choice == "3":
            date_format = "%Y-%m-%d"
            start_str = input("Start date (YYYY-MM-DD): ").strip()
            end_str = input("End date (YYYY-MM-DD): ").strip()
            try:
                start_date = datetime.strptime(start_str, date_format)
                end_date = datetime.strptime(end_str, date_format)
                if end_date < start_date:
                    print("End date must be on or after start date.")
                    return
            except ValueError:
                print("Invalid date format.")
                return
            filtered = [r for r in self.reports if start_date <= r.date.date() <= end_date]
            self.list_reports(filtered)
        else:
            print("Invalid choice.")

    def set_reference_point(self):
        print("\nSet reference point for distance calculations (default is 0.0, 0.0):")
        loc = self.input_location()
        if loc:
            self.reference_point = loc
            print(f"Reference point set to ({loc.latitude}, {loc.longitude})")
        else:
            print("Failed to set reference point.")

    def run(self):
        print("=== Natural Disaster Report CLI ===")
        while True:
            print("\nCommands:")
            print("  1 - Add new report")
            print("  2 - List all reports")
            print("  3 - Search reports")
            print("  4 - Set reference point")
            print("  0 - Exit")
            cmd = input("Enter command number: ").strip()
            if cmd == "1":
                self.add_report()
            elif cmd == "2":
                self.list_reports()
            elif cmd == "3":
                self.search_reports()
            elif cmd == "4":
                self.set_reference_point()
            elif cmd == "0":
                print("Exiting. Goodbye!")
                break
            else:
                print("Unknown command. Please try again.")

if __name__ == "__main__":
    cli = DisasterReportCLI()
    cli.run()

