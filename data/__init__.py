import csv
import os
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent

def get_regions_list():
	try:
		csv_path = os.path.join(base_dir, 'data', 'regions.csv')
		regions_list = []
		with open(csv_path, 'r') as csv_file:
			csv_reader = csv.DictReader(csv_file)
			for row in csv_reader:
				if int(row['seq']) in [25, 26]:
					continue
				regions_list.append({
					'seq': int(row['seq']),
					'region': row['region']
				})
		return regions_list
	except Exception as e:
		return []

def get_regions_list_full():
	try:
		csv_path = os.path.join(base_dir, 'data', 'regions.csv')
		regions_list = []
		with open(csv_path, 'r') as csv_file:
			csv_reader = csv.DictReader(csv_file)
			for row in csv_reader:
				regions_list.append({
					'seq': int(row['seq']),
					'region': row['region']
				})
		return regions_list
	except Exception as e:
		return []

def get_services_list():
	try:
		csv_path = os.path.join(base_dir, 'data', 'services.csv')
		services_list = []
		with open(csv_path, 'r') as csv_file:
			csv_reader = csv.DictReader(csv_file)
			for row in csv_reader:
				services_list.append({
					'seq': int(row['seq']),
					'service': row['service_type']
				})
		return services_list
	except Exception as e:
		return []

def get_type_of_work_list():
	try:
		csv_path = os.path.join(base_dir, 'data', 'typeofwork.csv')
		services_list = []
		with open(csv_path, 'r') as csv_file:
			csv_reader = csv.DictReader(csv_file)
			for row in csv_reader:
				services_list.append({
					'seq': int(row['seq']),
					'work_type': row['work_type']
				})
		return services_list
	except Exception as e:
		return []

def get_activities_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'activities.csv')
        activities_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                activities_list.append({
                    'seq': int(row['seq']),
                    'activity': row['activity']
                })
        return activities_list
    except Exception as e:
        return []

def get_activities_driving_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'activities_driving.csv')
        driving_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                driving_list.append({
                    'seq': int(row['seq']),
                    'driving_activity': row['driving_activity']
                })
        return driving_list
    except Exception as e:
        return []

def get_activities_administration_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'activities_administration.csv')
        admin_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                admin_list.append({
                    'seq': int(row['seq']),
                    'administration_activity': row['administration_activity']
                })
        return admin_list
    except Exception as e:
        return []

def get_activities_mantinance_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'activities_mantinance.csv')
        mantinance_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                mantinance_list.append({
                    'seq': int(row['seq']),
                    'mantinance_activity': row['mantinance_activity']
                })
        return mantinance_list
    except Exception as e:
        return []

def get_activities_home_cares_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'activities_home_cares.csv')
        home_cares_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                home_cares_list.append({
                    'seq': int(row['seq']),
                    'home_cares_activity': row['home_cares_activity']
                })
        return home_cares_list
    except Exception as e:
        return []

def get_activities_technology_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'activities_technology.csv')
        technology_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                technology_list.append({
                    'seq': int(row['seq']),
                    'technology_activity': row['technology_activity']
                })
        return technology_list
    except Exception as e:
        return []

def get_activities_event_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'activities_event.csv')
        event_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                event_list.append({
                    'seq': int(row['seq']),
                    'event_activity': row['event_activity']
                })
        return event_list
    except Exception as e:
        return []

def get_activities_hospitality_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'activities_hospitality.csv')
        hospitality_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                hospitality_list.append({
                    'seq': int(row['seq']),
                    'hospitality_activity': row['hospitality_activity']
                })
        return hospitality_list
    except Exception as e:
        return []

def get_activities_support_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'activities_support.csv')
        support_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                support_list.append({
                    'seq': int(row['seq']),
                    'support_activity': row['support_activity']
                })
        return support_list
    except Exception as e:
        return []

def get_activities_financial_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'activities_financial.csv')
        financial_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                financial_list.append({
                    'seq': int(row['seq']),
                    'financial_activity': row['financial_activity']
                })
        return financial_list
    except Exception as e:
        return []

def get_activities_other_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'activities_other.csv')
        other_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                other_list.append({
                    'seq': int(row['seq']),
                    'other_activity': row['other_activity']
                })
        return other_list
    except Exception as e:
        return []

def get_activities_sport_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'activities_sport.csv')
        sport_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                sport_list.append({
                    'seq': int(row['seq']),
                    'sport_activity': row['sport_activity']
                })
        return sport_list
    except Exception as e:
        return []

def get_activities_group_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'activities_group.csv')
        group_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                group_list.append({
                    'seq': int(row['seq']),
                    'group_activity': row['group_activity']
                })
        return group_list
    except Exception as e:
        return []

def get_transport_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'transport.csv')
        transport_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                transport_list.append({
                    'seq': int(row['seq']),
                    'transport': row['transport']
                })
        return transport_list
    except Exception as e:
        return []

def get_time_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'time.csv')
        time_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                time_list.append({
                    'seq': int(row['seq']),
                    'time': row['time']
                })
        return time_list
    except Exception as e:
        return []

def get_refer_from_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'refer_from.csv')
        refer_from_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                refer_from_list.append({
                    'seq': int(row['seq']),
                    'refer_from': row['refer_from']
                })
        return refer_from_list
    except Exception as e:
        return []

def get_labour_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'labour.csv')
        labour_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                labour_list.append({
                    'seq': int(row['seq']),
                    'labour': row['labour']
                })
        return labour_list
    except Exception as e:
        return []

def get_ethnic_origin_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'ethnic_origin.csv')
        ethnic_origin_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                ethnic_origin_list.append({
                    'seq': int(row['seq']),
                    'ethnic_origin': row['ethnic_origin']
                })
        return ethnic_origin_list
    except Exception as e:
        return []

def get_days_list():
    try:
        csv_path = os.path.join(base_dir, 'data', 'days.csv')
        days_list = []
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                days_list.append({
                    'seq': int(row['seq']),
                    'day': row['day']
                })
        return days_list
    except Exception as e:
        return []
