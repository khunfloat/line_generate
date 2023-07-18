routes_1 = [
    "ฐานถาปัตหน้า → เดินในสนาม → ฐานถาปัตกลาง",
    "ฐานถาปัตกลาง → เดินในสนาม → ฐานถาปัตหลัง",
    "ฐานถาปัตหลัง → ทางเดินหน้าลานพระรูป → ฐานวิทยาหลัง",
    "ฐานวิทยาหลัง → เดินในสนาม → ฐานวิทยากลาง",
    "ฐานวิทยากลาง → เดินในสนาม → ฐานวิทยาหน้า",
    "ฐานวิทยาหน้า → ทางเดินข้างสระน้ำ → ฐานถาปัตหน้า",
]

routes_2 = [
    "ฐานจามถาปัต → เดินวงเวียนตามเข็ม → ทางเดินข้างหอประชุมจุฬา → ฐานหอฬ.หลัง",
    "ฐานหอฬ.หลัง → ข้ามถนน → ฐานมหาหน้า",
    "ฐานมหาหน้า → ทางเดินข้างถนน → ฐานมหาหลัง",
    "ฐานมหาหลัง → ข้ามถนน → ฐานสระน้ำ",
    "ฐานสระน้ำ → ข้ามถนน → ทางเดินฝั่งคณะ → ข้ามถนน → ฐานหอฬ.หน้า",
    "ฐานหอฬ.หน้า → เดินวงเวียนตามเข็ม → ฐานจามถาปัต",
]

routes_3 = [
    "ฐานจามวิทยา → ข้ามถนน → ฐานโต๊ะเซน",
    "ฐานโต๊ะเซน → ทางเดินโต๊ะเซน → ฐานรวมใจ",
    "ฐานรวมใจ → ข้ามถนน → ฐานโต๊ะเซน",
    "ฐานโต๊ะเซน → ข้ามถนน → ทางขึ้นศาลาลานจักร → ฐานจักรหลุม",
    "ฐานจักรหลุม → ทางเดินลานจักรฝั่งวิทยา → ฐานจักรเดิน",
    "ฐานจักรเดิน → ทางเดินข้างตึกจักรพงษ์ → เลี้ยวตามหอนาฬิกา → ฐานจามวิทยา",
]

baan_1 = ["T", "J", "F", "H", "R", "K"]
baan_2 = ["C", "A", "B", "P", "E", "Dog"]
baan_3 = ["M", "L", "Q", "S", "G", "N"]


def sub_create(routes, baan, loop):
    output = []
    state = routes[loop % 6 :] + routes[: loop % 6]
    for index in range(6):
        output.append(f"บ้าน {baan[index]}: {state[index]}")
    return output


def create_route(loops=5):
    file = open("line_dry.txt", "w")
    result = []

    for loop in range(loops):
        # baan 1
        pool1 = sub_create(routes_1, baan_1, loop)

        # baan 2
        pool2 = sub_create(routes_2, baan_2, loop)

        # baan 3
        pool3 = sub_create(routes_3, baan_3, loop)

        all_pool = sorted(pool1 + pool2 + pool3)

        result.append(all_pool)

        for i in all_pool:
            file.write(i + "\n")
        file.write("---------------- \n")
    file.close()


create_route()