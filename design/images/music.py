import json, base64, sys, subprocess
model, prompt, out = sys.argv[1], sys.argv[2], sys.argv[3]
body={"contents":[{"parts":[{"text":prompt}]}],"generationConfig":{"responseModalities":["AUDIO"]}}
open('music-body.json','w').write(json.dumps(body))
r=subprocess.run(["curl","-sS","-w","\n%{http_code}","-H","Content-Type: application/json",f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent","-d","@music-body.json"],capture_output=True,text=True)
payload,code=r.stdout.rsplit("\n",1)
if code!="200": print("HTTP",code,payload[:700]); sys.exit(1)
d=json.loads(payload)
for part in d["candidates"][0]["content"]["parts"]:
    if "inlineData" in part:
        mt=part["inlineData"]["mimeType"]; open(out,"wb").write(base64.b64decode(part["inlineData"]["data"])); print("saved",out,mt); break
else: print("no audio", json.dumps(d)[:700])
