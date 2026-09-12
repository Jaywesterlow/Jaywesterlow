import json, base64, sys, subprocess, os
model = sys.argv[1]; prompt = sys.argv[2]; out = sys.argv[3]; ar = sys.argv[4] if len(sys.argv)>4 else "4:5"
body = {"contents":[{"parts":[{"text":prompt}]}],
        "generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":ar}}}
r = subprocess.run(["curl","-sS","-w","\n%{http_code}","-H","Content-Type: application/json",
    f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent","-d",json.dumps(body)],capture_output=True,text=True)
payload, code = r.stdout.rsplit("\n",1)
if code != "200":
    print("HTTP", code, payload[:600]); sys.exit(1)
d = json.loads(payload)
for part in d["candidates"][0]["content"]["parts"]:
    if "inlineData" in part:
        open(out,"wb").write(base64.b64decode(part["inlineData"]["data"])); print("saved", out, part["inlineData"]["mimeType"]); break
else:
    print("no image in response", json.dumps(d)[:600])
