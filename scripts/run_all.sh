#!/bin/bash

# Initialize
source ../agrisakha/bin/activate
export PYTHONPATH=$PWD/..

# Run all systems
echo "Testing Voice AI..."
python3 -m voice_ai.core --test

echo -e "\nTesting Credit Scoring..."
python3 -m credit_scoring.engine --demo

echo -e "\nTesting Soil Analysis..."
python3 -m edge_computing.soil --sample test_data/soil_sample1.json

echo -e "\nAll systems operational!"