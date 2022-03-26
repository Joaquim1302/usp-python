secs = int(
    input("Por favor, entre com o número de segundos que deseja converter: "))

secs_dia = 24 * 3600
ds = secs // secs_dia
secs_rest = secs % secs_dia

hs = secs_rest // 3600
secs_rest = secs % 3600

mins = secs_rest // 60

secs_rest %= 60

print(str(ds), "dias,", str(hs), "horas,",
      str(mins), "minutos e", str(secs_rest), "segundos.")
