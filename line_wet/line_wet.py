# RED
routes_2 = [
    "ฐาน 1 → เดินในสนาม → ฐาน 2",
    "ฐาน 2 → เดินในสนาม → ฐาน 3",
    "ฐาน 3 → เดินเลาะสระน้ำ → เดินทางตรงข้ามสถาปัตย์ → ฐาน 1",
]

# ORANGE
routes_1 = [
    "ฐาน 4 → เดินทางเท้า → ฐาน 5",
    "ฐาน 5 → เดินข้ามถนน → ฐาน 6",
    "ฐาน 6 →  เดินข้ามถนนไปฝั่งตึก 3 → ทางเท้าฝั่งตึก 3 → ฐาน 4",
]

# PURPLE
routes_4 = [
    "ฐาน 7 → เดินในสนาม → ฐาน 8",
    "ฐาน 8 → เดินในสนาม → ฐาน 9",
    "ฐาน 9 → ทางเท้าฝั่งคณะวิทยาศาสตร์→ ฐาน 7",
]

# PINK
routes_3 = [
    "ฐาน 10 → เดินทางเท้า → ฐาน 11",
    "ฐาน 11 → เดินข้ามถนน → ฐาน 12",
    "ฐาน 12 →  เดินทางข้างตึกจักรพงษ์ → ฐาน 10",
]

# DARKBLUE
routes_6 = [
    "ฐาน 13 → เดินข้ามถนน → เดินถนนข้างโรงอาหาร → ฐาน 14",
    "ฐาน 14 → เดินถนนหลังตึก 100 ปี → ฐาน 15",
    "ฐาน 15 → เดินถนนข้างตึก 4, ตึก 100, โรงอาหาร → เดินข้ามถนน → ฐาน 13",
]

# BLUE
routes_5 = [
    "ฐาน 16 → เดินข้ามถนน → ฐาน 17",
    "ฐาน 17 → เดินในสนาม → ฐาน 18",
    "ฐาน 18 →  เดินข้ามถนน → ฐาน 16",
]

baan_1 = ["01", "02", "03"]
baan_2 = ["04", "05", "06"]
baan_3 = ["07", "08", "09"]
baan_4 = ["10", "11", "12"]
baan_5 = ["13", "14", "15"]
baan_6 = ["16", "17", "18"]


def sub_create(routes, baan, loop):
    output = []
    state = routes[loop % 3 :] + routes[: loop % 3]
    for index in range(3):
        output.append(f"Cluster {baan[index]}: {state[index]}")
    return output


def create_route(loops=5):
    file = open("line_wet.txt", "w")
    result = []

    for loop in range(loops):
        # baan 1
        pool1 = sub_create(routes_1, baan_1, loop)

        # baan 2
        pool2 = sub_create(routes_2, baan_2, loop)

        # baan 3
        pool3 = sub_create(routes_3, baan_3, loop)

        # baan 4
        pool4 = sub_create(routes_4, baan_4, loop)

        # baan 5
        pool5 = sub_create(routes_5, baan_5, loop)

        # baan 6
        pool6 = sub_create(routes_6, baan_6, loop)

        all_pool = sorted(pool1 + pool2 + pool3 + pool4 + pool5 + pool6)

        result.append(all_pool)

        for i in all_pool:
            file.write(i + "\n")
        file.write("---------------- \n")
    file.close()


create_route(3)
