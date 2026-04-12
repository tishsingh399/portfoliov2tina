import os
import shutil

target_dir = "/Users/tinasingh/Desktop/tina-portfolio/case-studies/images"
pngs = [f for f in os.listdir(target_dir) if f.endswith('.png')]

target_names = [
    "shield-before-state.png",
    "shield-audit-findings.png",
    "shield-token-layers.png",
    "shield-placeholder-1.png",
    "shield-placeholder-2.png",
    "shield-placeholder-3.png",
    "shield-placeholder-4.png",
    "nav-audit.png",
    "nav-framework.png",
    "alert-hierarchy.png",
    "alert-variants.png",
    "login-before-after.png"
]

unused_dir = os.path.join(target_dir, "unused")
os.makedirs(unused_dir, exist_ok=True)

specific_mappings = {
    "Navigation.png": "nav-framework.png",
    "Token and interaction logic.png": "shield-token-layers.png",
    "Tokens.png": "shield-before-state.png",
    "what iowneddesignsystem rebuild.png": "shield-placeholder-1.png"
}

for k, v in specific_mappings.items():
    if k in pngs and v in target_names:
        shutil.move(os.path.join(target_dir, k), os.path.join(target_dir, v))
        pngs.remove(k)
        target_names.remove(v)

for png in pngs:
    src = os.path.join(target_dir, png)
    if target_names:
        dst = os.path.join(target_dir, target_names.pop(0))
        shutil.move(src, dst)
    else:
        shutil.move(src, os.path.join(unused_dir, png))

print("Done mapping images!")
