collection = {
    'S01': {'name': 'Hoàng', 'salary': 1351},
    'S02': {'name': 'Thành', 'salary': 1541},
    'S03': {'name': 'Bảo', 'salary': 1413},
    'S04': {'name': 'Tú', 'salary': 1613}
}

# Xuất danh sách nhân viên theo lương giảm dần:
employee = sorted(collection.items(), key=lambda value: value[1]['salary'], reverse=True)
print(employee)
for i in employee:
    print(i[0], i[1]['name'], i[1]['salary'])
