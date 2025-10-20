"""
F1 Driver Analysis System with Jolpica F1 API Integration
=========================================================

This version uses the Jolpica F1 API (replacement for Ergast API)
which provides current F1 data including 2025 season data.

Author: AI Assistant
Date: 2024
"""

import requests
import json
import time
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional
from datetime import datetime
import math

class JolpicaF1APIClient:
    """Client for interacting with Jolpica F1 API (Ergast replacement)"""
    
    def __init__(self):
        self.base_url = "https://api.jolpi.ca/ergast/f1"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'F1-Analysis-System/1.0',
            'Accept': 'application/json'
        })
    
    def get_current_season_drivers(self) -> List[Dict]:
        """Get current season drivers from Jolpica API"""
        try:
            current_year = datetime.now().year
            
            # Try current year first
            url = f"{self.base_url}/{current_year}/drivers.json"
            print(f"Fetching drivers from: {url}")
            response = self.session.get(url, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                drivers = data['MRData']['DriverTable']['Drivers']
                if drivers:
                    print(f"Successfully fetched {len(drivers)} drivers for {current_year}")
                    return drivers
            
            # Fall back to previous year if current year has no data
            previous_year = current_year - 1
            print(f"No data available for {current_year}, trying {previous_year}...")
            url = f"{self.base_url}/{previous_year}/drivers.json"
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            
            data = response.json()
            drivers = data['MRData']['DriverTable']['Drivers']
            
            print(f"Successfully fetched {len(drivers)} drivers for {previous_year}")
            return drivers
            
        except requests.RequestException as e:
            print(f"Error fetching drivers: {e}")
            return []
    
    def get_driver_standings(self, year: int = None) -> List[Dict]:
        """Get driver standings for a specific year"""
        if year is None:
            year = datetime.now().year
            
        try:
            url = f"{self.base_url}/{year}/driverStandings.json"
            response = self.session.get(url, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                standings = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
                if standings:
                    print(f"Successfully fetched driver standings for {year}")
                    return standings
            
            # Fall back to previous year
            previous_year = year - 1
            url = f"{self.base_url}/{previous_year}/driverStandings.json"
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            
            data = response.json()
            standings = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
            
            print(f"Successfully fetched driver standings for {previous_year}")
            return standings
            
        except requests.RequestException as e:
            print(f"Error fetching standings: {e}")
            return []
    
    def get_constructor_standings(self, year: int = None) -> List[Dict]:
        """Get constructor standings for a specific year"""
        if year is None:
            year = datetime.now().year
            
        try:
            url = f"{self.base_url}/{year}/constructorStandings.json"
            response = self.session.get(url, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                standings = data['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']
                if standings:
                    print(f"Successfully fetched constructor standings for {year}")
                    return standings
            
            # Fall back to previous year
            previous_year = year - 1
            url = f"{self.base_url}/{previous_year}/constructorStandings.json"
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            
            data = response.json()
            standings = data['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']
            
            print(f"Successfully fetched constructor standings for {previous_year}")
            return standings
            
        except requests.RequestException as e:
            print(f"Error fetching constructor standings: {e}")
            return []
    
    def get_race_results(self, year: int = None, round_num: int = None) -> List[Dict]:
        """Get race results for a specific year and round"""
        if year is None:
            year = datetime.now().year
            
        try:
            if round_num:
                url = f"{self.base_url}/{year}/{round_num}/results.json"
            else:
                url = f"{self.base_url}/{year}/results.json"
                
            response = self.session.get(url, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                races = data['MRData']['RaceTable']['Races']
                if races:
                    print(f"Successfully fetched race results for {year}")
                    return races
            
            # Fall back to previous year
            previous_year = year - 1
            if round_num:
                url = f"{self.base_url}/{previous_year}/{round_num}/results.json"
            else:
                url = f"{self.base_url}/{previous_year}/results.json"
                
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            
            data = response.json()
            races = data['MRData']['RaceTable']['Races']
            
            print(f"Successfully fetched race results for {previous_year}")
            return races
            
        except requests.RequestException as e:
            print(f"Error fetching race results: {e}")
            return []
    
    def get_qualifying_results(self, year: int = None, round_num: int = None) -> List[Dict]:
        """Get qualifying results for a specific year and round"""
        if year is None:
            year = datetime.now().year
            
        try:
            if round_num:
                url = f"{self.base_url}/{year}/{round_num}/qualifying.json"
            else:
                url = f"{self.base_url}/{year}/qualifying.json"
                
            response = self.session.get(url, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                races = data['MRData']['RaceTable']['Races']
                if races:
                    print(f"Successfully fetched qualifying results for {year}")
                    return races
            
            # Fall back to previous year
            previous_year = year - 1
            if round_num:
                url = f"{self.base_url}/{previous_year}/{round_num}/qualifying.json"
            else:
                url = f"{self.base_url}/{previous_year}/qualifying.json"
                
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            
            data = response.json()
            races = data['MRData']['RaceTable']['Races']
            
            print(f"Successfully fetched qualifying results for {previous_year}")
            return races
            
        except requests.RequestException as e:
            print(f"Error fetching qualifying results: {e}")
            return []

@dataclass
class APIDriverStats:
    """Driver statistics from API data"""
    driver_id: str
    name: str
    nationality: str
    constructor: str
    points: int
    position: int
    wins: int
    podiums: int
    fastest_laps: int
    pole_positions: int
    races_completed: int
    average_finish: float
    average_qualifying: float

class JolpicaF1AnalysisSystem:
    """Enhanced F1 analysis system with Jolpica API integration"""
    
    def __init__(self):
        self.api_client = JolpicaF1APIClient()
        self.drivers_data = {}
        self.standings_data = {}
        self.race_results = {}
        self.qualifying_results = {}
        self.current_season = None
        
    def get_current_season(self) -> int:
        """Get the current season being used for analysis"""
        return self.current_season or datetime.now().year
        
    def load_current_data(self) -> bool:
        """Load current season data from Jolpica API"""
        print("Loading current F1 data from Jolpica API...")
        
        # Load drivers
        drivers = self.api_client.get_current_season_drivers()
        if not drivers:
            print("Failed to load drivers data")
            return False
        
        # Determine which season we're actually using
        current_year = datetime.now().year
        self.current_season = current_year  # Will be updated if fallback was used
        
        # Load standings
        standings = self.api_client.get_driver_standings()
        if not standings:
            print("Failed to load standings data")
            return False
        
        # Load race results
        race_results = self.api_client.get_race_results()
        if not race_results:
            print("Failed to load race results")
            return False
        
        # Load qualifying results
        qualifying_results = self.api_client.get_qualifying_results()
        if not qualifying_results:
            print("Failed to load qualifying results")
            return False
        
        # Process and store data
        self._process_drivers_data(drivers)
        self._process_standings_data(standings)
        self._process_race_results(race_results)
        self._process_qualifying_results(qualifying_results)
        
        print(f"Successfully loaded all data for {self.current_season} season!")
        return True
    
    def _process_drivers_data(self, drivers: List[Dict]):
        """Process drivers data from API"""
        for driver in drivers:
            driver_id = driver['driverId']
            self.drivers_data[driver_id] = {
                'name': f"{driver['givenName']} {driver['familyName']}",
                'nationality': driver['nationality'],
                'date_of_birth': driver.get('dateOfBirth', ''),
                'permanent_number': driver.get('permanentNumber', ''),
                'url': driver.get('url', '')
            }
    
    def _process_standings_data(self, standings: List[Dict]):
        """Process standings data from API"""
        for standing in standings:
            driver_id = standing['Driver']['driverId']
            constructor = standing['Constructors'][0]['name']
            
            self.standings_data[driver_id] = {
                'position': int(standing['position']),
                'points': float(standing['points']),
                'wins': int(standing['wins']),
                'constructor': constructor
            }
    
    def _process_race_results(self, races: List[Dict]):
        """Process race results from API"""
        for race in races:
            round_num = race['round']
            race_name = race['raceName']
            
            self.race_results[round_num] = {
                'race_name': race_name,
                'date': race['date'],
                'circuit': race['Circuit']['circuitName'],
                'results': race['Results']
            }
    
    def _process_qualifying_results(self, races: List[Dict]):
        """Process qualifying results from API"""
        for race in races:
            round_num = race['round']
            race_name = race['raceName']
            
            self.qualifying_results[round_num] = {
                'race_name': race_name,
                'date': race['date'],
                'circuit': race['Circuit']['circuitName'],
                'results': race['QualifyingResults']
            }
    
    def calculate_driver_statistics(self, driver_id: str) -> Optional[APIDriverStats]:
        """Calculate comprehensive driver statistics from API data"""
        if driver_id not in self.drivers_data or driver_id not in self.standings_data:
            return None
        
        driver_info = self.drivers_data[driver_id]
        standing_info = self.standings_data[driver_id]
        
        # Calculate additional statistics from race results
        podiums = 0
        fastest_laps = 0
        pole_positions = 0
        total_finish_positions = []
        total_qualifying_positions = []
        races_completed = 0
        
        for round_num, race_data in self.race_results.items():
            for result in race_data['results']:
                if result['Driver']['driverId'] == driver_id:
                    finish_pos = int(result['position'])
                    total_finish_positions.append(finish_pos)
                    races_completed += 1
                    
                    # Count podiums (positions 1-3)
                    if finish_pos <= 3:
                        podiums += 1
                    
                    # Check for fastest lap
                    if result.get('FastestLap', {}).get('rank') == '1':
                        fastest_laps += 1
        
        # Calculate qualifying statistics
        for round_num, quali_data in self.qualifying_results.items():
            for result in quali_data['results']:
                if result['Driver']['driverId'] == driver_id:
                    quali_pos = int(result['position'])
                    total_qualifying_positions.append(quali_pos)
                    
                    # Count pole positions
                    if quali_pos == 1:
                        pole_positions += 1
        
        # Calculate averages
        avg_finish = sum(total_finish_positions) / len(total_finish_positions) if total_finish_positions else 0
        avg_qualifying = sum(total_qualifying_positions) / len(total_qualifying_positions) if total_qualifying_positions else 0
        
        return APIDriverStats(
            driver_id=driver_id,
            name=driver_info['name'],
            nationality=driver_info['nationality'],
            constructor=standing_info['constructor'],
            points=standing_info['points'],
            position=standing_info['position'],
            wins=standing_info['wins'],
            podiums=podiums,
            fastest_laps=fastest_laps,
            pole_positions=pole_positions,
            races_completed=races_completed,
            average_finish=avg_finish,
            average_qualifying=avg_qualifying
        )
    
    def calculate_race_win_probability(self, driver_stats: APIDriverStats) -> float:
        """Calculate race win probability based on API data"""
        # Base probability from current performance
        base_prob = 0.0
        
        # Points-based probability (higher points = higher chance)
        max_points = max(s['points'] for s in self.standings_data.values())
        points_ratio = driver_stats.points / max_points if max_points > 0 else 0
        
        # Win rate probability
        win_rate = driver_stats.wins / driver_stats.races_completed if driver_stats.races_completed > 0 else 0
        
        # Podium rate probability
        podium_rate = driver_stats.podiums / driver_stats.races_completed if driver_stats.races_completed > 0 else 0
        
        # Qualifying performance probability
        quali_score = max(0, 100 - (driver_stats.average_qualifying - 1) * 5)
        
        # Combined probability calculation
        base_prob = (points_ratio * 0.4 + win_rate * 0.3 + podium_rate * 0.2 + quali_score/100 * 0.1) * 100
        
        # Apply softmax normalization across all drivers
        all_scores = []
        for driver_id in self.standings_data.keys():
            stats = self.calculate_driver_statistics(driver_id)
            if stats:
                max_points = max(s['points'] for s in self.standings_data.values())
                points_ratio = stats.points / max_points if max_points > 0 else 0
                win_rate = stats.wins / stats.races_completed if stats.races_completed > 0 else 0
                podium_rate = stats.podiums / stats.races_completed if stats.races_completed > 0 else 0
                quali_score = max(0, 100 - (stats.average_qualifying - 1) * 5)
                score = points_ratio * 0.4 + win_rate * 0.3 + podium_rate * 0.2 + quali_score/100 * 0.1
                all_scores.append(score)
        
        # Softmax normalization
        if all_scores:
            max_score = max(all_scores)
            exp_scores = [math.exp(score - max_score) for score in all_scores]
            sum_exp = sum(exp_scores)
            
            driver_index = list(self.standings_data.keys()).index(driver_stats.driver_id)
            probability = exp_scores[driver_index] / sum_exp * 100
            return probability
        
        return base_prob
    
    def calculate_championship_probability(self, driver_stats: APIDriverStats) -> float:
        """Calculate championship probability based on API data"""
        current_points = driver_stats.points
        position = driver_stats.position
        
        # Get leader's points
        leader_points = max(s['points'] for s in self.standings_data.values())
        points_gap = leader_points - current_points
        
        # Base probability from current position
        if position == 1:
            base_prob = 0.7
        elif position <= 3:
            base_prob = 0.2
        elif position <= 6:
            base_prob = 0.05
        else:
            base_prob = 0.01
        
        # Adjust based on performance consistency
        consistency_factor = 1.0 - (driver_stats.average_finish - 1) / 20
        consistency_factor = max(0.1, min(1.0, consistency_factor))
        
        # Adjust based on win rate
        win_rate_factor = driver_stats.wins / driver_stats.races_completed if driver_stats.races_completed > 0 else 0
        win_rate_factor = max(0.1, min(1.0, win_rate_factor + 0.1))
        
        # Calculate final probability
        probability = base_prob * consistency_factor * win_rate_factor
        
        # Apply diminishing returns for large points gaps
        if points_gap > 0:
            gap_factor = max(0.1, 1 - (points_gap / (6 * 25)))
            probability *= gap_factor
        
        return min(probability * 100, 100)
    
    def get_driver_comparison(self) -> List[Tuple[APIDriverStats, float, float]]:
        """Get all drivers with their win and championship probabilities"""
        results = []
        
        for driver_id in self.standings_data.keys():
            stats = self.calculate_driver_statistics(driver_id)
            if stats:
                race_prob = self.calculate_race_win_probability(stats)
                champ_prob = self.calculate_championship_probability(stats)
                results.append((stats, race_prob, champ_prob))
        
        # Sort by race win probability (descending)
        results.sort(key=lambda x: x[1], reverse=True)
        return results
    
    def display_driver_analysis(self, driver_name: str = None):
        """Display comprehensive driver analysis"""
        if not self.standings_data:
            print("No data loaded. Please run load_current_data() first.")
            return
        
        season = self.get_current_season()
        print(f"\nF1 Analysis for {season} Season (Jolpica API)")
        print("=" * 60)
        
        if driver_name:
            # Find driver by name
            driver_id = None
            for did, dinfo in self.drivers_data.items():
                if driver_name.lower() in dinfo['name'].lower():
                    driver_id = did
                    break
            
            if not driver_id:
                print(f"Driver '{driver_name}' not found.")
                return
            
            stats = self.calculate_driver_statistics(driver_id)
            if stats:
                self._display_single_driver(stats)
        else:
            # Display all drivers
            print(f"\nALL DRIVERS ANALYSIS - {season} Season")
            print("=" * 80)
            print(f"{'Driver':<25} {'Team':<20} {'Points':<8} {'Pos':<4} {'Race Win %':<12} {'Championship %':<15}")
            print("=" * 80)
            
            comparisons = self.get_driver_comparison()
            for stats, race_prob, champ_prob in comparisons:
                print(f"{stats.name:<25} {stats.constructor:<20} {stats.points:<8.0f} {stats.position:<4} {race_prob:<12.1f} {champ_prob:<15.1f}")
    
    def _display_single_driver(self, stats: APIDriverStats):
        """Display detailed analysis for a single driver"""
        race_prob = self.calculate_race_win_probability(stats)
        champ_prob = self.calculate_championship_probability(stats)
        
        print(f"\nDETAILED ANALYSIS - {stats.name}")
        print("-" * 50)
        print(f"Team: {stats.constructor}")
        print(f"Nationality: {stats.nationality}")
        print(f"Current Points: {stats.points}")
        print(f"Championship Position: {stats.position}")
        print(f"Races Completed: {stats.races_completed}")
        
        print(f"\nPerformance Statistics:")
        print(f"  Wins: {stats.wins}")
        print(f"  Podiums: {stats.podiums}")
        print(f"  Pole Positions: {stats.pole_positions}")
        print(f"  Fastest Laps: {stats.fastest_laps}")
        print(f"  Average Finish Position: {stats.average_finish:.1f}")
        print(f"  Average Qualifying Position: {stats.average_qualifying:.1f}")
        
        print(f"\nProbabilities:")
        print(f"  Race Win Probability: {race_prob:.1f}%")
        print(f"  Championship Probability: {champ_prob:.1f}%")

def main():
    """Main function for Jolpica API-integrated F1 analysis system"""
    print("F1 Driver Analysis System with Jolpica API Integration")
    print("=" * 70)
    print("Using Jolpica F1 API (Ergast replacement) for current data")
    print("=" * 70)
    
    system = JolpicaF1AnalysisSystem()
    
    # Load current data
    if not system.load_current_data():
        print("Failed to load data. Please check your internet connection.")
        return
    
    season = system.get_current_season()
    print(f"\nAnalyzing {season} F1 Season Data")
    print("Note: Using Jolpica API for up-to-date information")
    
    while True:
        print(f"\nAvailable Analysis Options ({season} Season):")
        print("1. View All Drivers Analysis")
        print("2. Analyze Specific Driver")
        print("3. Refresh Data from API")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            system.display_driver_analysis()
        
        elif choice == '2':
            driver_name = input("Enter driver name: ").strip()
            system.display_driver_analysis(driver_name)
        
        elif choice == '3':
            print("Refreshing data from Jolpica API...")
            if system.load_current_data():
                season = system.get_current_season()
                print(f"Data refreshed successfully! Now analyzing {season} season.")
            else:
                print("Failed to refresh data.")
        
        elif choice == '4':
            print("\nThanks for using the F1 Analysis System!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
