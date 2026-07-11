## Port

`port` is the TCP port used by the local audio HTTP server. The default is `5050`.

After changing the port, restart Anki and update the custom audio source URL in Yomitan to use the same port. For example, with port `18080`:

```text
http://127.0.0.1:18080/?term={term}&reading={reading}
```

This setting is separate from `user_files/config.json`, which configures audio sources and their paths.
