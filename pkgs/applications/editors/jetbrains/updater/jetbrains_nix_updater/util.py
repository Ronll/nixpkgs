import subprocess


def run_command(cmd: list[str], **kwargs) -> str:
    result = subprocess.run(cmd, capture_output=True, check=True, text=True, **kwargs)
    return result.stdout.strip()


def convert_hash_to_sri(base32: str) -> str:
    return run_command(["nix-hash", "--to-sri", "--type", "sha256", base32])


def ensure_is_list(x):
    if type(x) is not list:
        return [x]
    return x


def one_or_more(x):
    return x if isinstance(x, list) else [x]
