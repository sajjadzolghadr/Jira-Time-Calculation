import csv
from collections import defaultdict
from django.shortcuts import render
from .forms import UploadCSVForm

def jira_page(request):
    result = None

    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            monthly_hours = form.cleaned_data['monthly_work_hours']
            decoded_file = uploaded_file.read().decode('utf-8').splitlines()
            csv_reader = csv.reader(decoded_file)

            data_list = list(csv_reader)

            nahaE = []
            for line in data_list[1:]:
                if len(line) > 37:
                    nahaE.append(line[13] + ' ' + line[37])

            sums = defaultdict(int)
            for item in nahaE:
                parts = item.split()
                if len(parts) == 2:
                    name, value = parts[0], int(parts[1])
                    sums[name] += value

            # تقسیم بر 3600
            for name in sums:
                sums[name] //= 3600
            
            result = []
            for name, worked_hours in sums.items():
                shortage = max(0, monthly_hours - worked_hours)
                overtime = max(0, worked_hours - monthly_hours)
                result.append({
                    'name': name,
                    'worked_hours': worked_hours,
                    'shortage': shortage,
                    'overtime': overtime,
                })

            result = sorted(result, key=lambda x: x['worked_hours'], reverse=True)

    else:
        form = UploadCSVForm()

    return render(request, 'jira.html', {'form': form, 'result': result})