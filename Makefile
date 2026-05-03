# Базовый путь к исходникам
SRC_DIR = backend/src

# Список таблиц для проекта Pet Store
TABLES = categories products suppliers inventory customers orders order_items

# Команда для создания файлов в указанной папке
# Использование: make gen folder=имя_папки
gen:
	@if [ -z "$(folder)" ]; then \
		echo "Ошибка: Укажите целевую папку. Пример: make gen folder=repositories"; \
	else \
		TARGET_PATH=$(SRC_DIR)/$(folder); \
		mkdir -p $$TARGET_PATH; \
		for table in $(TABLES); do \
			touch $$TARGET_PATH/$$table.py; \
			echo "Создан: $$TARGET_PATH/$$table.py"; \
		done; \
		if [ ! -f $$TARGET_PATH/__init__.py ]; then \
			touch $$TARGET_PATH/__init__.py; \
			echo "Создан: $$TARGET_PATH/__init__.py"; \
		fi; \
		echo "--- Все файлы для слоя '$(folder)' успешно созданы ---"; \
	fi

# Очистка конкретной папки (по желанию)
# Использование: make clean_folder folder=имя_папки
clean_folder:
	@if [ -n "$(folder)" ]; then \
		rm -rf $(SRC_DIR)/$(folder)/*.py; \
		echo "Папка $(folder) очищена."; \
	fi