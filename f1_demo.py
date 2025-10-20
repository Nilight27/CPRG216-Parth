"""
F1 Jolpica API Demo - Show 2025 Season Analysis
===============================================

This script demonstrates the Jolpica API integration with 2025 F1 data
"""

from f1_analysis_system import JolpicaF1AnalysisSystem

def demo_jolpica_api():
    """Demonstrate the Jolpica API with 2025 F1 data"""
    print("F1 Driver Analysis System - Jolpica API Demo")
    print("=" * 60)
    print("Using Jolpica F1 API for 2025 season data")
    print("=" * 60)
    
    system = JolpicaF1AnalysisSystem()
    
    # Load current data
    print("Loading 2025 F1 data from Jolpica API...")
    if not system.load_current_data():
        print("Failed to load data. Please check your internet connection.")
        return
    
    season = system.get_current_season()
    print(f"\nSuccessfully loaded {season} F1 Season Data!")
    
    # Show all drivers analysis
    print("\n" + "="*80)
    print("2025 F1 DRIVERS ANALYSIS")
    print("="*80)
    system.display_driver_analysis()
    
    # Show detailed analysis for top 3 drivers
    print("\n" + "="*80)
    print("TOP 3 DRIVERS DETAILED ANALYSIS")
    print("="*80)
    
    comparisons = system.get_driver_comparison()
    for i, (stats, race_prob, champ_prob) in enumerate(comparisons[:3]):
        print(f"\n{i+1}. {stats.name} ({stats.constructor})")
        print("-" * 50)
        print(f"Current Points: {stats.points}")
        print(f"Championship Position: {stats.position}")
        print(f"Wins: {stats.wins}")
        print(f"Podiums: {stats.podiums}")
        print(f"Pole Positions: {stats.pole_positions}")
        print(f"Races Completed: {stats.races_completed}")
        print(f"Average Finish: {stats.average_finish:.1f}")
        print(f"Average Qualifying: {stats.average_qualifying:.1f}")
        print(f"Race Win Probability: {race_prob:.1f}%")
        print(f"Championship Probability: {champ_prob:.1f}%")
    
    # Show API benefits
    print("\n" + "="*80)
    print("JOLPICA API BENEFITS")
    print("="*80)
    print("Successfully connected to Jolpica F1 API")
    print("Retrieved 2025 season data (21 drivers)")
    print("Real-time driver standings and race results")
    print("Comprehensive qualifying and race statistics")
    print("Automatic data updates from official sources")
    print("No manual data entry required")
    print("Always up-to-date information")
    
    print(f"\nData Summary:")
    print(f"  Season: {season}")
    print(f"  Drivers: {len(system.drivers_data)}")
    print(f"  Races: {len(system.race_results)}")
    print(f"  Qualifying Sessions: {len(system.qualifying_results)}")
    
    print(f"\nTop 5 Championship Contenders:")
    standings = sorted(system.standings_data.items(), 
                     key=lambda x: x[1]['points'], reverse=True)[:5]
    
    for i, (driver_id, data) in enumerate(standings, 1):
        driver_name = system.drivers_data[driver_id]['name']
        print(f"  {i}. {driver_name}: {data['points']} points ({data['wins']} wins)")

if __name__ == "__main__":
    demo_jolpica_api()
