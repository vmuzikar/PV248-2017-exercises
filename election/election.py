import json
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from math import pi


def bar_plot(data_json):
    data = {
        "name": [],
        "number": [],
        "share": [],
        "color": []
    }

    below_one = 0

    for party in data_json:
        if party["share"] < 1:
            below_one += party["share"]
            continue

        if "short" in party:
            name = party["short"]
        else:
            name = party["name"]

        if "color" in party:
            color = party["color"]
        else:
            color = "grey"

        data["name"].append(name)
        data["number"].append(len(data["number"]) + 1)
        data["share"].append(party["share"])
        data["color"].append(color)

    data["name"].append("Others")
    data["number"].append(len(data["number"]) + 1)
    data["share"].append(below_one)
    data["color"].append("grey")

    src = ColumnDataSource(data=data)
    plot = figure()
    plot.vbar(x="number", top="share", width=0.7, color="color", legend="name", source=src)

    return plot


def pie_chart(data_json):
    data = {
        "name": [],
        "start": [],
        "stop": [],
        "color": []
    }

    data_json.append({
        "name": "Others",
        "share": 0,
        "color": "grey"
    })

    last_angle = 0

    for party in data_json:
        if party["share"] < 1 and party["name"] is not "Others":
            data_json[-1]["share"] += party["share"]
            continue

        if "short" in party:
            name = party["short"]
        else:
            name = party["name"]

        if "color" in party:
            color = party["color"]
        else:
            color = "grey"

        current_angle = last_angle + party["share"] / 100 * 2 * pi

        data["name"].append(name)
        data["start"].append(last_angle)
        data["stop"].append(current_angle)
        data["color"].append(color)

        last_angle = current_angle

    src = ColumnDataSource(data=data)
    plot = figure(x_range=(-10, 10))
    plot.wedge(x=0, y=0, radius=5, start_angle="start", end_angle="stop", color="color", legend="name", source=src)

    return plot

def main():
    f = open("election.json", encoding="utf8")
    j = json.load(f)
    f.close()

    show(pie_chart(j))


if __name__ == "__main__":
    main()