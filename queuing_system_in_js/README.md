## 0. Install a redis instance

This directory contains the Redis persistence file `dump.rdb` required by the project.

### Expected result

When loading `dump.rdb` into Redis and running `GET Holberton`, it should return `School`.

### Reproduce locally (Linux / WSL)

Download, extract, and compile Redis 6.0.10:

```bash
wget http://download.redis.io/releases/redis-6.0.10.tar.gz
tar xzf redis-6.0.10.tar.gz
cd redis-6.0.10
make
```

Start Redis in the background:

```bash
src/redis-server &
```

Verify the server:

```bash
src/redis-cli ping
```

Expected output:

```text
PONG
```

Set the required key:

```bash
src/redis-cli set Holberton School
src/redis-cli get Holberton
```

Save to generate `dump.rdb` in the current directory:

```bash
src/redis-cli save
```

Stop Redis (replace with the `redis-server` PID):

```bash
kill [PID_OF_Redis_Server]
```

Copy `dump.rdb` into this directory (`queuing_system_in_js/`).

