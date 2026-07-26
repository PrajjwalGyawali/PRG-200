bs_months = ["Baisakh","Jestha","Ashadh","Shrawan","Bhadra","Ashwin",
             "Kartik","Mangsir","Poush","Magh","Falgun","Chaitra"]
ad_months = ["January","February","March","April","May","June",
             "July","August","September","October","November","December"]

def ordinal(n):
    if 11 <= n % 100 <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"

def convert_date(date_str, from_cal, to_cal):
    year, month, day = date_str.split("-")
    year, month, day = int(year), int(month), int(day)

    if from_cal == to_cal:
        return date_str

    if from_cal == "AD" and to_cal == "BS":
        year = year + 56
    elif from_cal == "BS" and to_cal == "AD":
        year = year - 56

    return year, month, day

def format_date(year, month, day, cal, style):
    if style == "iso":
        return f"{year:04d}-{month:02d}-{day:02d}"
    if cal == "BS":
        return f"{ordinal(day)} {bs_months[month-1]}, {year} BS"
    return f"{ordinal(day)} {ad_months[month-1]}, {year} AD"

customers = [
    {"name": "Ramesh Thapa", "date": "1985-06-24", "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Sunita Karki", "date": "2055-09-10", "cal": "BS", "need": "AD", "style": "iso"},
    {"name": "Bikash Rai", "date": "1998-11-30", "cal": "AD", "need": "BS", "style": "nepali"},
    {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD", "style": "full"},
]

for c in customers:
    result = convert_date(c["date"], c["cal"], c["need"])
    if isinstance(result, str):
        converted = result
    else:
        year, month, day = result
        converted = format_date(year, month, day, c["need"], c["style"])
    print(f"{c['name']}  | Original: {c['date']} {c['cal']} | Converted: {converted}")