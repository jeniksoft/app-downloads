# Aplikace

Každá aplikace má vlastní složku:

```text
apps/<app-id>/
```

Složka aplikace obsahuje veřejný setup, popis, návod k použití a případné poznámky k verzi. Zdrojové kódy ani LLM/model weights sem nepatří.

## Ke Stažení

| Aplikace | Verze | Setup | Dokumentace | SHA-256 |
| --- | --- | --- | --- | --- |
| Codex VeraCrypt Startup Mount | 1.0.140 | [VeraCryptStartupMountSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/veracrypt-startup-mount/VeraCryptStartupMountSetup.exe) | [Popis a návod](veracrypt-startup-mount/README.md) | [`EC0D3B00...30353E4E`](../checksums/SHA256SUMS.txt) |
| Jarvis | 0.1.169 | [JarvisSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/personal-codex-fallback-host/JarvisSetup.exe) | [Popis a návod](personal-codex-fallback-host/README.md) | [`EB8E120D...C75BB1CF`](../checksums/SHA256SUMS.txt) |
| Windows Update Restart Guard | 1.0.98 | [WindowsUpdateRestartGuardSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/windows-update-restart-guard/WindowsUpdateRestartGuardSetup.exe) | [Popis a návod](windows-update-restart-guard/README.md) | [`20F29F02...09FC36C6`](../checksums/SHA256SUMS.txt) |

Tabulky zkracují SHA-256 kvůli čitelnosti. Plný hash je v app `update.json` a `checksums/SHA256SUMS.txt`.
