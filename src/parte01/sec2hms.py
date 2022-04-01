secs = int(input("Segundos:"))

secs_dia = 24 * 3600
ds = secs // secs_dia
secs_rest = secs % secs_dia

hs = secs_rest // 3600
secs_rest = secs % 3600

mins = secs_rest // 60

secs_rest %= 60

print(str(ds) + "dias " + str(hs) + "h " + str(mins) + "m " + str(secs_rest) + "s")
