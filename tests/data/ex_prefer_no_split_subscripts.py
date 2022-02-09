x["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

x[x["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"] or "xxxxxxx"] = "xxxxxxxxxxxxxxxxxxxxxxxxx"

# output

x["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"] = (
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
)

x[x["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"] or "xxxxxxx"] = (
    "xxxxxxxxxxxxxxxxxxxxxxxxx"
)
