#/bin/bash
#
# Name: GENOMELINK LOCAL CLIENT SETUP
# Ver : 1.0.1
#

pip install -qr requirements.txt
export GENOMELINK_CLIENT_ID=CLOmX1sWF2BRgmSgdP8L3VZlWaLqiGQnfFmVgqRl
export GENOMELINK_CLIENT_SECRET=GGwsYiUDKB9ESvGYXL9a7c1vQEtPsBgDXWwBDPxph5cYtaD9QceB2PRBZc7b1OEOuSUXEVWcRG9CbwtsKxTM07YTkol010glqrp3xhaYcsmmBCv55SPNxububAMidVtm
export GENOMELINK_CALLBACK_URL="http://127.0.0.1:5000/callback"
python app.py 
