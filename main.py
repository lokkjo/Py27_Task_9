import datetime

class Open_with_time_count:
	def __init__(self, file_path, encoding='utf8',
				 t_start=datetime.datetime.now()):
		self.file_path = file_path
		self.encoding = encoding
		self.t_start = t_start

	def __enter__(self):
		print(f'Время запуска кода: {self.t_start}')
		# print(self.t_start)
		self.file = open(self.file_path)
		return self.file

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.file.close()
		t_end = datetime.datetime.now()
		print(f'Время окончания работы: {t_end}')
		print(f'Обработка файла заняла '
			  f'{t_end.microsecond - self.t_start.microsecond} '
			  f'микросекунд.')

with Open_with_time_count('third_crusade.txt', 'rt') as f:
	i_1 = 0
	i_2 = 0
	for line in f:
		if 'Third Crusade' in line:
			i_1 += 1
			with open('crusade_context.txt', 'a') as doc:
				doc.write(f'{i_1}: {line}\n')
		elif 'Richard' in line:
			i_2 += 1
			with open('richard_context.txt', 'a') as doc:
				doc.write(f'{i_2}: {line}\n')
	print(f'\nКрестовый поход упоминается {i_1} раз.')
	print(f'Ричард упоминается {i_2} раз.\n')






# t_start = datetime.datetime.now().microsecond
# print(t)