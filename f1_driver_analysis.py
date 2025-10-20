"""
F1 Driver Analysis and Prediction System
========================================

This system analyzes current F1 drivers, their performance stats, car capabilities,
and calculates probabilities for race wins and championship victories.

Author: AI Assistant
Date: 2024
"""

import random
import math
from dataclasses import dataclass
from typing import Dict, List, Tuple
from enum import Enum

class TrackType(Enum):
    """Different types of F1 tracks"""
    STREET = "street"
    PERMANENT = "permanent"
    HIGH_SPEED = "high_speed"
    TECHNICAL = "technical"

@dataclass
class CarSpecs:
    """Car specifications and performance metrics"""
    engine_power: float  # Horsepower
    aerodynamics: float  # Downforce efficiency (0-100)
    reliability: float   # Reliability score (0-100)
    tire_management: float  # Tire degradation resistance (0-100)
    fuel_efficiency: float  # Fuel consumption efficiency (0-100)
    chassis_balance: float  # Overall car balance (0-100)
    
    def overall_performance(self) -> float:
        """Calculate overall car performance score"""
        weights = {
            'engine_power': 0.25,
            'aerodynamics': 0.20,
            'reliability': 0.15,
            'tire_management': 0.15,
            'fuel_efficiency': 0.10,
            'chassis_balance': 0.15
        }
        
        return sum(getattr(self, attr) * weight for attr, weight in weights.items())

@dataclass
class DriverStats:
    """Driver performance statistics"""
    qualifying_avg: float      # Average qualifying position
    race_finish_avg: float     # Average race finish position
    points_per_race: float     # Average points per race
    podiums: int               # Number of podiums this season
    wins: int                  # Number of wins this season
    fastest_laps: int          # Number of fastest laps
    consistency: float         # Consistency score (0-100)
    wet_weather_skill: float   # Wet weather performance (0-100)
    overtaking_ability: float  # Overtaking skill (0-100)
    race_craft: float         # Strategic race management (0-100)
    
    def overall_skill(self) -> float:
        """Calculate overall driver skill score"""
        # Normalize positions (lower is better)
        quali_score = max(0, 100 - (self.qualifying_avg - 1) * 5)
        race_score = max(0, 100 - (self.race_finish_avg - 1) * 4)
        
        weights = {
            'quali_score': 0.20,
            'race_score': 0.25,
            'points_per_race': 0.15,
            'consistency': 0.15,
            'wet_weather_skill': 0.10,
            'overtaking_ability': 0.10,
            'race_craft': 0.05
        }
        
        return (quali_score * weights['quali_score'] + 
                race_score * weights['race_score'] + 
                self.points_per_race * weights['points_per_race'] + 
                self.consistency * weights['consistency'] + 
                self.wet_weather_skill * weights['wet_weather_skill'] + 
                self.overtaking_ability * weights['overtaking_ability'] + 
                self.race_craft * weights['race_craft'])

@dataclass
class Driver:
    """Complete driver profile with stats and car"""
    name: str
    team: str
    nationality: str
    age: int
    current_points: int
    championship_position: int
    stats: DriverStats
    car: CarSpecs
    
    def total_performance_score(self) -> float:
        """Calculate combined driver + car performance score"""
        driver_score = self.stats.overall_skill()
        car_score = self.car.overall_performance()
        
        # Weight: 60% driver skill, 40% car performance
        return driver_score * 0.6 + car_score * 0.4

class F1AnalysisSystem:
    """Main F1 analysis and prediction system"""
    
    def __init__(self):
        self.drivers = self._initialize_drivers()
        self.track_characteristics = self._initialize_track_types()
    
    def _initialize_drivers(self) -> List[Driver]:
        """Initialize current F1 drivers with realistic 2024 data"""
        drivers_data = [
            # Top teams
            {
                'name': 'Max Verstappen', 'team': 'Red Bull Racing', 'nationality': 'Dutch', 'age': 26,
                'current_points': 524, 'championship_position': 1,
                'stats': DriverStats(1.2, 1.8, 26.2, 19, 19, 9, 95, 90, 85, 92),
                'car': CarSpecs(1000, 95, 98, 92, 88, 96)
            },
            {
                'name': 'Sergio Perez', 'team': 'Red Bull Racing', 'nationality': 'Mexican', 'age': 34,
                'current_points': 285, 'championship_position': 2,
                'stats': DriverStats(3.8, 4.2, 14.3, 8, 2, 2, 78, 75, 80, 85),
                'car': CarSpecs(1000, 95, 98, 92, 88, 96)
            },
            {
                'name': 'Lewis Hamilton', 'team': 'Mercedes', 'nationality': 'British', 'age': 39,
                'current_points': 234, 'championship_position': 3,
                'stats': DriverStats(4.5, 5.1, 11.7, 6, 0, 1, 88, 95, 90, 95),
                'car': CarSpecs(980, 88, 85, 82, 85, 90)
            },
            {
                'name': 'George Russell', 'team': 'Mercedes', 'nationality': 'British', 'age': 26,
                'current_points': 175, 'championship_position': 4,
                'stats': DriverStats(5.2, 6.8, 8.8, 3, 0, 0, 82, 80, 85, 88),
                'car': CarSpecs(980, 88, 85, 82, 85, 90)
            },
            {
                'name': 'Carlos Sainz', 'team': 'Ferrari', 'nationality': 'Spanish', 'age': 29,
                'current_points': 200, 'championship_position': 5,
                'stats': DriverStats(3.9, 4.8, 10.0, 7, 1, 2, 85, 75, 80, 82),
                'car': CarSpecs(990, 92, 80, 85, 82, 88)
            },
            {
                'name': 'Charles Leclerc', 'team': 'Ferrari', 'nationality': 'Monegasque', 'age': 26,
                'current_points': 190, 'championship_position': 6,
                'stats': DriverStats(2.8, 4.5, 9.5, 6, 0, 1, 80, 85, 88, 85),
                'car': CarSpecs(990, 92, 80, 85, 82, 88)
            },
            {
                'name': 'Lando Norris', 'team': 'McLaren', 'nationality': 'British', 'age': 24,
                'current_points': 169, 'championship_position': 7,
                'stats': DriverStats(4.1, 5.5, 8.5, 4, 0, 1, 88, 80, 85, 90),
                'car': CarSpecs(970, 90, 88, 90, 85, 85)
            },
            {
                'name': 'Oscar Piastri', 'team': 'McLaren', 'nationality': 'Australian', 'age': 23,
                'current_points': 97, 'championship_position': 8,
                'stats': DriverStats(6.8, 8.2, 4.9, 2, 0, 0, 75, 70, 75, 80),
                'car': CarSpecs(970, 90, 88, 90, 85, 85)
            },
            {
                'name': 'Fernando Alonso', 'team': 'Aston Martin', 'nationality': 'Spanish', 'age': 43,
                'current_points': 74, 'championship_position': 9,
                'stats': DriverStats(8.5, 9.8, 3.7, 1, 0, 0, 85, 90, 88, 95),
                'car': CarSpecs(960, 85, 90, 80, 80, 82)
            },
            {
                'name': 'Lance Stroll', 'team': 'Aston Martin', 'nationality': 'Canadian', 'age': 25,
                'current_points': 53, 'championship_position': 10,
                'stats': DriverStats(12.1, 13.5, 2.7, 0, 0, 0, 70, 75, 70, 75),
                'car': CarSpecs(960, 85, 90, 80, 80, 82)
            },
            # Midfield teams
            {
                'name': 'Pierre Gasly', 'team': 'Alpine', 'nationality': 'French', 'age': 28,
                'current_points': 62, 'championship_position': 11,
                'stats': DriverStats(10.8, 12.2, 3.1, 0, 0, 0, 78, 80, 75, 80),
                'car': CarSpecs(950, 82, 85, 78, 85, 80)
            },
            {
                'name': 'Esteban Ocon', 'team': 'Alpine', 'nationality': 'French', 'age': 28,
                'current_points': 58, 'championship_position': 12,
                'stats': DriverStats(11.2, 12.8, 2.9, 0, 0, 0, 75, 75, 80, 78),
                'car': CarSpecs(950, 82, 85, 78, 85, 80)
            },
            {
                'name': 'Alexander Albon', 'team': 'Williams', 'nationality': 'Thai', 'age': 28,
                'current_points': 27, 'championship_position': 13,
                'stats': DriverStats(13.5, 15.2, 1.4, 0, 0, 0, 80, 75, 85, 82),
                'car': CarSpecs(920, 75, 88, 70, 90, 75)
            },
            {
                'name': 'Yuki Tsunoda', 'team': 'AlphaTauri', 'nationality': 'Japanese', 'age': 24,
                'current_points': 14, 'championship_position': 14,
                'stats': DriverStats(14.8, 16.5, 0.7, 0, 0, 0, 70, 70, 75, 75),
                'car': CarSpecs(930, 78, 82, 75, 85, 78)
            },
            {
                'name': 'Nico Hulkenberg', 'team': 'Haas', 'nationality': 'German', 'age': 36,
                'current_points': 9, 'championship_position': 15,
                'stats': DriverStats(15.2, 17.8, 0.5, 0, 0, 0, 75, 80, 70, 80),
                'car': CarSpecs(940, 80, 75, 72, 88, 78)
            },
            {
                'name': 'Valtteri Bottas', 'team': 'Sauber', 'nationality': 'Finnish', 'age': 35,
                'current_points': 10, 'championship_position': 16,
                'stats': DriverStats(16.1, 18.2, 0.5, 0, 0, 0, 80, 75, 75, 85),
                'car': CarSpecs(925, 75, 85, 70, 85, 75)
            },
            {
                'name': 'Zhou Guanyu', 'team': 'Sauber', 'nationality': 'Chinese', 'age': 25,
                'current_points': 6, 'championship_position': 17,
                'stats': DriverStats(17.5, 19.1, 0.3, 0, 0, 0, 70, 70, 70, 75),
                'car': CarSpecs(925, 75, 85, 70, 85, 75)
            },
            {
                'name': 'Kevin Magnussen', 'team': 'Haas', 'nationality': 'Danish', 'age': 32,
                'current_points': 3, 'championship_position': 18,
                'stats': DriverStats(18.2, 19.8, 0.2, 0, 0, 0, 72, 75, 75, 78),
                'car': CarSpecs(940, 80, 75, 72, 88, 78)
            },
            {
                'name': 'Logan Sargeant', 'team': 'Williams', 'nationality': 'American', 'age': 23,
                'current_points': 1, 'championship_position': 19,
                'stats': DriverStats(19.1, 20.5, 0.1, 0, 0, 0, 65, 65, 70, 70),
                'car': CarSpecs(920, 75, 88, 70, 90, 75)
            },
            {
                'name': 'Daniel Ricciardo', 'team': 'AlphaTauri', 'nationality': 'Australian', 'age': 35,
                'current_points': 0, 'championship_position': 20,
                'stats': DriverStats(18.8, 20.2, 0.0, 0, 0, 0, 75, 80, 80, 85),
                'car': CarSpecs(930, 78, 82, 75, 85, 78)
            }
        ]
        
        return [Driver(**data) for data in drivers_data]
    
    def _initialize_track_types(self) -> Dict[TrackType, Dict[str, float]]:
        """Initialize track characteristics that affect performance"""
        return {
            TrackType.STREET: {
                'aerodynamics_weight': 0.3,
                'engine_power_weight': 0.2,
                'reliability_weight': 0.25,
                'tire_management_weight': 0.15,
                'driver_skill_weight': 0.1
            },
            TrackType.PERMANENT: {
                'aerodynamics_weight': 0.25,
                'engine_power_weight': 0.25,
                'reliability_weight': 0.2,
                'tire_management_weight': 0.2,
                'driver_skill_weight': 0.1
            },
            TrackType.HIGH_SPEED: {
                'aerodynamics_weight': 0.35,
                'engine_power_weight': 0.3,
                'reliability_weight': 0.15,
                'tire_management_weight': 0.1,
                'driver_skill_weight': 0.1
            },
            TrackType.TECHNICAL: {
                'aerodynamics_weight': 0.2,
                'engine_power_weight': 0.15,
                'reliability_weight': 0.2,
                'tire_management_weight': 0.25,
                'driver_skill_weight': 0.2
            }
        }
    
    def calculate_race_win_probability(self, driver: Driver, track_type: TrackType = TrackType.PERMANENT) -> float:
        """Calculate probability of winning the next race"""
        weights = self.track_characteristics[track_type]
        
        # Calculate weighted performance score
        car_score = (
            driver.car.aerodynamics * weights['aerodynamics_weight'] +
            driver.car.engine_power * weights['engine_power_weight'] +
            driver.car.reliability * weights['reliability_weight'] +
            driver.car.tire_management * weights['tire_management_weight']
        )
        
        driver_score = driver.stats.overall_skill() * weights['driver_skill_weight']
        
        total_score = car_score + driver_score
        
        # Calculate relative probability compared to other drivers
        all_scores = []
        for d in self.drivers:
            d_car_score = (
                d.car.aerodynamics * weights['aerodynamics_weight'] +
                d.car.engine_power * weights['engine_power_weight'] +
                d.car.reliability * weights['reliability_weight'] +
                d.car.tire_management * weights['tire_management_weight']
            )
            d_driver_score = d.stats.overall_skill() * weights['driver_skill_weight']
            all_scores.append(d_car_score + d_driver_score)
        
        # Use softmax to convert scores to probabilities
        max_score = max(all_scores)
        exp_scores = [math.exp(score - max_score) for score in all_scores]
        sum_exp = sum(exp_scores)
        
        driver_index = self.drivers.index(driver)
        probability = exp_scores[driver_index] / sum_exp
        
        return probability * 100
    
    def calculate_championship_probability(self, driver: Driver, races_remaining: int = 6) -> float:
        """Calculate probability of winning the championship"""
        current_points = driver.current_points
        position = driver.championship_position
        
        # Get leader's points
        leader_points = max(d.current_points for d in self.drivers if d.championship_position == 1)
        
        # Calculate points gap
        points_gap = leader_points - current_points
        
        # Base probability from current position and points
        if position == 1:
            base_prob = 0.7  # Leader has high probability
        elif position <= 3:
            base_prob = 0.2  # Top 3 have reasonable chance
        elif position <= 6:
            base_prob = 0.05  # Midfield have small chance
        else:
            base_prob = 0.01  # Backmarkers have minimal chance
        
        # Adjust based on performance consistency
        consistency_factor = driver.stats.consistency / 100
        performance_factor = driver.total_performance_score() / 100
        
        # Calculate final probability
        probability = base_prob * consistency_factor * performance_factor
        
        # Apply diminishing returns for large points gaps
        if points_gap > 0:
            gap_factor = max(0.1, 1 - (points_gap / (races_remaining * 25)))
            probability *= gap_factor
        
        return min(probability * 100, 100)
    
    def get_driver_comparison(self) -> List[Tuple[Driver, float, float]]:
        """Get all drivers with their win and championship probabilities"""
        results = []
        for driver in self.drivers:
            race_prob = self.calculate_race_win_probability(driver)
            champ_prob = self.calculate_championship_probability(driver)
            results.append((driver, race_prob, champ_prob))
        
        # Sort by race win probability (descending)
        results.sort(key=lambda x: x[1], reverse=True)
        return results
    
    def get_top_performers(self, count: int = 10) -> List[Driver]:
        """Get top performing drivers by overall performance score"""
        sorted_drivers = sorted(self.drivers, key=lambda d: d.total_performance_score(), reverse=True)
        return sorted_drivers[:count]
    
    def analyze_team_performance(self) -> Dict[str, Dict]:
        """Analyze performance by team"""
        team_stats = {}
        
        for driver in self.drivers:
            team = driver.team
            if team not in team_stats:
                team_stats[team] = {
                    'drivers': [],
                    'total_points': 0,
                    'avg_performance': 0,
                    'car_performance': driver.car.overall_performance()
                }
            
            team_stats[team]['drivers'].append(driver.name)
            team_stats[team]['total_points'] += driver.current_points
            team_stats[team]['avg_performance'] += driver.total_performance_score()
        
        # Calculate averages
        for team in team_stats:
            driver_count = len(team_stats[team]['drivers'])
            team_stats[team]['avg_performance'] /= driver_count
        
        return team_stats

def main():
    """Main function to demonstrate the F1 analysis system"""
    print("F1 Driver Analysis and Prediction System")
    print("=" * 50)
    
    system = F1AnalysisSystem()
    
    while True:
        print("\nAvailable Analysis Options:")
        print("1. View Driver Comparison (Race Win & Championship Probabilities)")
        print("2. Analyze Specific Driver")
        print("3. View Top Performers")
        print("4. Team Performance Analysis")
        print("5. Calculate Probabilities for Different Track Types")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            print("\nDriver Comparison - Race Win & Championship Probabilities")
            print("-" * 70)
            print(f"{'Driver':<20} {'Team':<15} {'Race Win %':<12} {'Championship %':<15}")
            print("-" * 70)
            
            comparisons = system.get_driver_comparison()
            for driver, race_prob, champ_prob in comparisons:
                print(f"{driver.name:<20} {driver.team:<15} {race_prob:<12.1f} {champ_prob:<15.1f}")
        
        elif choice == '2':
            print("\nDriver Analysis")
            driver_name = input("Enter driver name: ").strip()
            
            driver = None
            for d in system.drivers:
                if driver_name.lower() in d.name.lower():
                    driver = d
                    break
            
            if driver:
                print(f"\nAnalysis for {driver.name}")
                print("-" * 40)
                print(f"Team: {driver.team}")
                print(f"Nationality: {driver.nationality}")
                print(f"Age: {driver.age}")
                print(f"Current Points: {driver.current_points}")
                print(f"Championship Position: {driver.championship_position}")
                print(f"Overall Performance Score: {driver.total_performance_score():.1f}")
                print(f"Driver Skill Score: {driver.stats.overall_skill():.1f}")
                print(f"Car Performance Score: {driver.car.overall_performance():.1f}")
                
                # Calculate probabilities for different track types
                print(f"\nRace Win Probabilities by Track Type:")
                for track_type in TrackType:
                    prob = system.calculate_race_win_probability(driver, track_type)
                    print(f"  {track_type.value.title()}: {prob:.1f}%")
                
                champ_prob = system.calculate_championship_probability(driver)
                print(f"\nChampionship Probability: {champ_prob:.1f}%")
            else:
                print("Driver not found!")
        
        elif choice == '3':
            print("\nTop Performers by Overall Performance Score")
            print("-" * 50)
            top_performers = system.get_top_performers(10)
            
            for i, driver in enumerate(top_performers, 1):
                score = driver.total_performance_score()
                print(f"{i:2d}. {driver.name:<20} ({driver.team}) - Score: {score:.1f}")
        
        elif choice == '4':
            print("\nTeam Performance Analysis")
            print("-" * 40)
            team_stats = system.analyze_team_performance()
            
            for team, stats in team_stats.items():
                print(f"\n{team}:")
                print(f"  Drivers: {', '.join(stats['drivers'])}")
                print(f"  Total Points: {stats['total_points']}")
                print(f"  Average Performance: {stats['avg_performance']:.1f}")
                print(f"  Car Performance: {stats['car_performance']:.1f}")
        
        elif choice == '5':
            print("\nTrack Type Analysis")
            print("Select a driver to analyze:")
            
            for i, driver in enumerate(system.drivers, 1):
                print(f"{i:2d}. {driver.name} ({driver.team})")
            
            try:
                driver_idx = int(input("\nEnter driver number: ")) - 1
                if 0 <= driver_idx < len(system.drivers):
                    driver = system.drivers[driver_idx]
                    print(f"\n{driver.name} - Win Probabilities by Track Type:")
                    print("-" * 50)
                    
                    for track_type in TrackType:
                        prob = system.calculate_race_win_probability(driver, track_type)
                        print(f"{track_type.value.title():<12}: {prob:>6.1f}%")
                else:
                    print("Invalid driver number!")
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == '6':
            print("\nThanks for using the F1 Analysis System!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
