from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route("/api/decode")
def decode_classplus():
    enc = request.args.get("q")
    if not enc:
        return jsonify({"success": False, "error": "Missing parameter q"}), 400

    try:
        enc = enc.strip().replace(' ', '+')
        missing_padding = len(enc) % 4
        if missing_padding:
            enc += '=' * (4 - missing_padding)

        decoded = base64.b64decode(enc).decode('utf-8')

        if ".m3u8" in decoded:
            return jsonify({
                "success": True,
                "status": "ok",
                "url": decoded
            })
        else:
            return jsonify({
                "success": False,
                "status": "error",
                "message": "Valid string but not a .m3u8 link",
                "decoded": decoded
            })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/")
def index():
    return "✅ Classplus Resolver API is live."

if __name__ == "__main__":
    app.run(debug=True)
