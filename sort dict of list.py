data = {
    'AI01': ['John', 3000],
    'AI09': ['Bill', 3500],
    'AI07': ['Bill', 2500],
    'AI03': ['Bill', 3800],
    'AI06': ['Bill', 4000],
}

def salary_value(item):
    return item[1][1]

# Xuất danh sách nhân viên theo lương tăng dần:
employee = sorted(data.items(), key=salary_value)
print(employee)
for i in employee:
    print(i[0], i[1][0], i[1][1])
