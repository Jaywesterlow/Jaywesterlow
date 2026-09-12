import json, base64, sys, subprocess, time
model, prompt, image, out = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
b64 = base64.b64encode(open(image,'rb').read()).decode()
body = {"instances":[{"prompt":prompt,"image":{"bytesBase64Encoded":b64,"mimeType":"image/jpeg"}}],
        "parameters":{"aspectRatio":"16:9","durationSeconds":8,"resolution":"1080p","personGeneration":"allow_adult"}}
def call(method, url, data=None):
    args=["curl","-sS","-w","\n%{http_code}","-X",method,"-H","Content-Type: application/json",url]
    if data is not None:
        open('veo-body.json','w').write(json.dumps(data)); args += ["-d", "@veo-body.json"]
    r=subprocess.run(args,capture_output=True,text=True); payload,code=r.stdout.rsplit("\n",1); return code, payload
code, payload = call("POST", f"https://generativelanguage.googleapis.com/v1beta/models/{model}:predictLongRunning", body)
if code != "200": print("HTTP", code, payload[:800]); sys.exit(1)
name = json.loads(payload)["name"]; print("operation", name)
for i in range(90):
    time.sleep(10)
    code, payload = call("GET", f"https://generativelanguage.googleapis.com/v1beta/{name}")
    d = json.loads(payload)
    if d.get("done"):
        if "error" in d: print("error", d["error"]); sys.exit(1)
        resp = d["response"]
        samples = resp.get("generateVideoResponse",{}).get("generatedSamples") or resp.get("generatedSamples") or []
        if not samples: print("no samples", json.dumps(resp)[:800]); sys.exit(1)
        uri = samples[0]["video"]["uri"]; print("uri", uri)
        r = subprocess.run(["curl","-sS","-L","-o",out,uri]); print("saved", out); break
    print("waiting", i*10, "s", d.get("metadata",{}))
