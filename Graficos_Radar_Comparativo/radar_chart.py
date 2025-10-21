from soccerplots.radar_chart import Radar

# Metricas a comparar
params = [
    'Pases Clave', '% Tiros a Puerta', 'Goles / Tiros', 'Recuperaciones',
    'Intercepciones', 'Regates Completados', '% Pases Éxitosos',
    'Pases Completados\n Bajo Presión', 'Pases Completados',
    'Pases Completados\n En Último Tercio'
]

# Rango de valores
ranges = [
    (0.0, 4), (0.0, 1), (0.00, 0.5), (0, 4.25), (0, 4.25),
    (0, 2.28), (0.0, 1), (0, 12), (0, 59), (0, 14.6)
]

# Valores 
values = [
    [
        a.loc[n1, 'Pases Clave'] / 6,
        a.loc[n1, '% Tiros a Puerta'],
        a.loc[n1, 'Goles / Tiros'],
        a.loc[n1, 'Recuperaciones'] / 124.8 * 20,
        a.loc[n1, 'Intercepciones'] / 124.8 * 20,
        a.loc[n1, 'Regates Completados'] / 6,
        a.loc[n1, '% acierto en pases'],
        a.loc[n1, 'pases bajo presion exito'] / 6,
        a.loc[n1, 'pases completados'] / 6,
        a.loc[n1, 'pases en el ultimo tercio exito'] / 6
    ],
    [
        a.loc[n2, 'Pases Clave'] / 7,
        a.loc[n2, '% Tiros a Puerta'],
        a.loc[n2, 'Goles / Tiros'],
        a.loc[n2, 'Recuperaciones'] / 103.6 * 20,
        a.loc[n2, 'Intercepciones'] / 103.6 * 20,
        a.loc[n2, 'Regates Completados'] / 7,
        a.loc[n2, '% acierto en pases'],
        a.loc[n2, 'pases bajo presion exito'] / 7,
        a.loc[n2, 'pases completados'] / 7,
        a.loc[n2, 'pases en el ultimo tercio exito'] / 7
    ]
]

# Configuración del radar
radar = Radar(background_color='none', fontfamily="Georgia")

title = dict(
    title_name='Hugo Fraile', title_color='#B6282F',
    subtitle_name='Porcinos FC', subtitle_color='#B6282F',
    title_fontsize=18, subtitle_fontsize=15,
    title_name_2='Pablo Hernández', title_color_2='#344D94',
    subtitle_name_2='Rayo De Barcelona', subtitle_color_2='#344D94'
)

endnote = ("Gráfico de radar realizado por: Pablo Pérez (@Pabloprz23) - @BigData_Kings\n"
           "Todas las métricas ofensivas están ajustadas al número de partidos jugados\n"
           "Todas las métricas defensivas están ajustadas por minutos de posesión del rival")

fig, ax = radar.plot_radar(
    ranges=ranges, params=params, values=values,
    radar_color=['#344D94', '#B6282F'],
    title=title, endnote=endnote,
    end_color="#121212",
    image_coord=[0.464, 0.81, 0.1, 0.075],
    compare=True
)
