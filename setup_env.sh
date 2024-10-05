
#!/bin/bash

# Create virtual environment
python -m venv venv

# Activate virtual environment based on OS
if [[ "$OSTYPE" == "msys" ]]; then
    # Windows
    source venv/Scripts/activate
else
    # Unix-based systems
    source venv/bin/activate
fi

# Install dependencies
pip install .
