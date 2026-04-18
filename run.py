"""
PayrollPH - Entry point

Run modes:
  python run.py         -> HTTPS port 5000 (required for GPS on iOS Safari)
  python run.py --http  -> plain HTTP (GPS will NOT work on iOS)

WHY HTTPS?
  iOS Safari blocks Geolocation on plain HTTP even if user grants permission.
  ssl_context='adhoc' generates a self-signed cert that satisfies iOS.

FIRST-TIME iOS SETUP:
  1. Open https://<your-pc-ip>:5000 on iPhone
  2. Tap "Show Details" -> "visit this website" -> "Visit Website" -> "Continue"
  3. GPS works normally after that.
"""

import sys
from app import create_app

app = create_app()

if __name__ == '__main__':
    use_http = '--http' in sys.argv
    port = 5000
    for i, arg in enumerate(sys.argv):
        if arg == '--port' and i + 1 < len(sys.argv):
            port = int(sys.argv[i + 1])

    if use_http:
        print("\n  WARNING: HTTP mode — GPS will NOT work on iOS Safari.\n")
        app.run(debug=True, host='0.0.0.0', port=port)
    else:
        print(f"\n  HTTPS mode active. Open: https://<your-ip>:{port}")
        print("  iOS first visit: tap 'Show Details' -> 'visit this website' -> Continue\n")
        app.run(debug=True, host='0.0.0.0', port=port, ssl_context='adhoc')
