# F1 Driver Analysis and Prediction System

A comprehensive Python system that analyzes current Formula 1 drivers, their performance statistics, car capabilities, and calculates probabilities for race wins and championship victories using the **Jolpica F1 API**.

## Features

### 🏎️ Driver Analysis
- **Current Season Stats**: Points, championship position, qualifying averages, race finishes
- **Performance Metrics**: Consistency, wet weather skill, overtaking ability, race craft
- **Car Specifications**: Engine power, aerodynamics, reliability, tire management

### 📊 Probability Calculations
- **Race Win Probability**: Calculates likelihood of winning the next Grand Prix
- **Championship Probability**: Estimates championship victory chances
- **Track Type Analysis**: Different probabilities for street circuits, high-speed tracks, technical circuits

### 🏢 Team Performance
- **Team Comparisons**: Total points, average performance, car performance
- **Driver Pairings**: Analysis of teammate performance

## Files

- `f1_analysis_system.py` - Main system with Jolpica API integration and all analysis algorithms
- `f1_demo.py` - Demonstration script showing 2025 season data
- `f1_driver_analysis.py` - Original static system (for comparison)
- `requirements.txt` - Dependencies
- `README.md` - This documentation file

## How to Use

### Running the Interactive System
```bash
python f1_analysis_system.py
```

This launches an interactive menu with options:
1. View Driver Comparison (Race Win & Championship Probabilities)
2. Analyze Specific Driver
3. Refresh Data from API
4. Exit

### Running the Demo
```bash
python f1_demo.py
```

This shows a comprehensive demonstration of the 2025 F1 season with real API data.

## System Components

### Driver Data Structure
Each driver includes:
- Personal info (name, team, nationality, age)
- Current season performance (points, position)
- Detailed statistics (qualifying, race finishes, podiums, wins)
- Skill ratings (consistency, wet weather, overtaking, race craft)

### Car Specifications
Each car is rated on:
- Engine Power (horsepower)
- Aerodynamics (downforce efficiency)
- Reliability (mechanical reliability)
- Tire Management (degradation resistance)
- Fuel Efficiency
- Chassis Balance

### Probability Algorithms

#### Race Win Probability
Uses weighted scoring based on:
- Driver skill (60% weight)
- Car performance (40% weight)
- Track characteristics (aerodynamics, engine power, reliability, tire management)
- Softmax normalization for probability distribution

#### Championship Probability
Considers:
- Current points and position
- Performance consistency
- Overall team/driver performance
- Points gap with races remaining

### Track Types
- **Street Circuits**: Monaco, Singapore (high aerodynamics, reliability)
- **Permanent Circuits**: Silverstone, Barcelona (balanced requirements)
- **High-Speed Tracks**: Monza, Baku (aerodynamics, engine power)
- **Technical Circuits**: Monaco, Hungary (tire management, driver skill)

## Sample Output (2025 Season)

```
ALL DRIVERS ANALYSIS - 2025 Season
================================================================================
Driver                    Team                 Points   Pos  Race Win %   Championship % 
================================================================================
Oscar Piastri             McLaren              346      1    15.1         56.0           
Lando Norris              McLaren              332      2    12.2         17.7           
Max Verstappen            Red Bull             306      3    10.6         13.2           
George Russell            Mercedes             252      4    7.0          1.7            
Charles Leclerc           Ferrari              192      5    3.9          0.0            
```

## Technical Details

- **Language**: Python 3.7+
- **Dependencies**: requests library
- **Data Source**: Jolpica F1 API (replacement for deprecated Ergast API)
- **Algorithms**: Weighted scoring, softmax normalization, statistical analysis
- **Real-time Data**: Automatic updates from official F1 sources

## API Integration Benefits

✅ **Always up-to-date data** from official F1 sources  
✅ **Automatic data updates** - no manual maintenance  
✅ **Real-time race results** and standings  
✅ **Comprehensive historical data** from 1950 onwards  
✅ **Professional-grade accuracy** with verified results  
✅ **No manual data entry** required  

## Customization

The system can be easily customized by:
- Modifying probability calculation weights
- Adding new track types
- Updating performance metrics
- Extending analysis algorithms

## Future Enhancements

Potential improvements:
- Machine learning models for predictions
- Weather condition factors
- Real-time updates during race weekends
- Visualization charts and graphs
- Integration with other racing series

## License

This project is for educational and demonstration purposes.
