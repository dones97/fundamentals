"""
Test script to verify the setup is correct before running the app
"""

import sys
import os

def test_python_version():
    """Check Python version"""
    print("Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} (OK)")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor}.{version.micro} (Need 3.8+)")
        return False

def test_dependencies():
    """Check if required packages are installed"""
    print("\nChecking dependencies...")
    required = {
        'streamlit': 'streamlit',
        'anthropic': 'anthropic',
        'PyPDF2': 'PyPDF2',
        'plotly': 'plotly',
        'pandas': 'pandas'
    }

    missing = []
    for package, import_name in required.items():
        try:
            __import__(import_name)
            print(f"✓ {package}")
        except ImportError:
            print(f"✗ {package} (missing)")
            missing.append(package)

    if missing:
        print(f"\n⚠ Missing packages: {', '.join(missing)}")
        print("Run: pip install -r requirements.txt")
        return False
    return True

def test_api_key():
    """Check if API key is configured"""
    print("\nChecking API key configuration...")

    # Check .env file
    env_file = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            content = f.read()
            if 'ANTHROPIC_API_KEY' in content and 'your_api_key_here' not in content:
                print("✓ .env file exists with API key")
                return True
            else:
                print("✗ .env file exists but API key not set")
                return False

    # Check environment variable
    if os.environ.get('ANTHROPIC_API_KEY'):
        print("✓ ANTHROPIC_API_KEY environment variable set")
        return True

    print("✗ API key not found")
    print("  Create .env file: cp .env.example .env")
    print("  Then add your API key to .env")
    return False

def test_file_structure():
    """Check if all required files exist"""
    print("\nChecking file structure...")
    required_files = [
        'app.py',
        'visualizations.py',
        'requirements.txt',
        '.gitignore',
        'README.md'
    ]

    missing = []
    for file in required_files:
        file_path = os.path.join(os.path.dirname(__file__), file)
        if os.path.exists(file_path):
            print(f"✓ {file}")
        else:
            print(f"✗ {file} (missing)")
            missing.append(file)

    return len(missing) == 0

def main():
    print("=" * 60)
    print("Stock Fundamentals Analyzer - Setup Test")
    print("=" * 60)

    tests = [
        ("Python Version", test_python_version),
        ("Dependencies", test_dependencies),
        ("File Structure", test_file_structure),
        ("API Key", test_api_key)
    ]

    results = []
    for name, test_func in tests:
        result = test_func()
        results.append((name, result))

    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)

    all_passed = True
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{name}: {status}")
        if not result:
            all_passed = False

    print("=" * 60)

    if all_passed:
        print("\n🎉 All tests passed! You're ready to run the app.")
        print("\nRun: streamlit run app.py")
    else:
        print("\n⚠ Some tests failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("  - Install dependencies: pip install -r requirements.txt")
        print("  - Set up API key: cp .env.example .env (then edit .env)")
        print("  - Ensure all files are present")

    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
