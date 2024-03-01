echo "Setting up the initial environment for your project..."

# Create virtual environment
echo "Creating virtual environment..."
python -m venv .venv

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/Scripts/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements_dev.txt

# Additional setup steps can go here

pip freeze

echo "Setup completed successfully."
