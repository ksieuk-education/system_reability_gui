import PyQt6.QtCore as pyqt6_qtcore
import PyQt6.QtWidgets as pyqt6_qtwidgets
from pydantic import ValidationError

import lib.app.split_settings.ui as app_split_settings_ui
import lib.methods.config as methods_config
import lib.ui.repositories as ui_repositories


class UiService(pyqt6_qtwidgets.QMainWindow, ui_repositories.Ui_MainWindow):
    def __init__(self, settings: app_split_settings_ui.UISettings, parent=None):
        super().__init__(parent)
        self.settings = settings
        self.setupUi(self)
        self.list_input.setSpacing(5)
        self.pb_calculate.clicked.connect(self.on_calculate)
        self.method_selected_model, self.method_selected = None, None
        self.text_entry.setText("Здесь будет результат работы программы")
        self.picture_obj = None
        self.cb_variants.addItems((f"Вариант №{i}" for i in range(1, self.settings.variants_count + 1)))
        self.cb_labs.addItems((f"Лабораторная работа №{i}" for i in range(1, self.settings.labs_count + 1)))
        self.cb_labs.activated.connect(self.on_lab)
        self.cb_variants.activated.connect(self.on_variant)
        self.lab_number = 1
        self.variant_number = 1
        self.methods = methods_config.LAB_3_METHODS
        self.connect_list_widget()

    def on_variant(self, value):
        self.variant_number = value + 1
        if self.lab_number == 3:
            self.set_schema_image()

    def set_schema_image(self):
        self.delete_image()
        if self.lab_number != 3:
            return
        image = ui_repositories.ImageViewer(
            str(self.settings.third_lab_schemas_path / f"Вариант {self.variant_number}.png")
        )
        self.layout_output_pictures.addWidget(image)
        self.picture_obj = image

    def on_lab(self, value):
        self.lab_number = value + 1
        self.delete_image()
        if self.lab_number == 2:
            self.methods = methods_config.LAB_2_METHODS

        if self.lab_number == 3:
            self.methods = methods_config.LAB_3_METHODS
            self.set_schema_image()
        self.set_methods()

    def create_fields_input(
        self, titles: list[str], values_names: list[str], values_default: list[methods_config.FIELD_DEFAULT_TYPE]
    ):
        self.list_input.clear()
        for i in range(len(titles)):
            self.create_field_input(i, titles[i], values_names[i], values_default[i])

    def create_field_input(
        self,
        field_number: int,
        title: str,
        value_name: str,
        value_default: methods_config.FIELD_DEFAULT_TYPE = None,
    ):
        item = pyqt6_qtwidgets.QListWidgetItem()
        item.setTextAlignment(pyqt6_qtcore.Qt.AlignmentFlag.AlignHCenter)
        self.list_input.addItem(item)
        widget = ui_repositories.CustomWidget(field_number, title, value_name, value_default)
        self.list_input.setItemWidget(item, widget)

    def set_methods(self):
        self.list_methods.clear()
        self.list_methods.addItems(list(self.methods.keys()))
        self.text_entry.setText("Здесь будет результат работы программы")

    def connect_list_widget(self) -> None:
        self.set_methods()
        self.list_methods.itemDoubleClicked.connect(self.select_method)

    def select_method(self, item: pyqt6_qtwidgets.QListWidgetItem) -> None:
        self.delete_image()
        self.text_entry.setText("Здесь будет результат работы программы")

        method_title = item.text()
        assert method_title in self.methods

        self.method_selected_model, self.method_selected = self.methods[method_title]
        model_schema = self.method_selected_model.model_json_schema()
        if "required" in model_schema:
            model_schema.pop("required")
        titles = [
            value["description"]
            for value in model_schema["properties"].values()
            if value["description"] != "Not expected"
        ]
        values_names = list(model_schema["properties"].keys())
        values_default = [value.get("default") for value in model_schema["properties"].values()]
        self.create_fields_input(titles, values_names, values_default)
        self.set_schema_image()

    def get_input_text(self) -> list[str]:
        if not self.method_selected_model:
            raise ValueError
        items = [self.list_input.item(row) for row in range(self.list_input.count())]
        input_values = {
            self.list_input.itemWidget(item).text()[0]: self.list_input.itemWidget(item).text()[1]  # type: ignore
            for item in items
        }
        input_values["variant"] = self.variant_number
        try:
            values_validated = self.method_selected_model.model_validate(input_values)
        except AttributeError:
            raise ValueError("Ошибка: Ни одного параметра не введено")
        return values_validated

    @classmethod
    def __get_error_message(cls, errors: list):
        error_messages = []
        for error in errors:
            message = error.get("msg")
            message = f"Ошибка валидации типа {message.split()[-1]}" if message.startswith("value is not") else message
            error_messages.append(f"{message}. Поле: {', '.join(error.get('loc'))}")
        return "\n".join(error_messages)

    def on_calculate(self):
        if not self.method_selected:
            self.text_entry.setText("Сначала нужно выбрать метод")
            return
        try:
            result = self.method_selected(self.get_input_text())
            if isinstance(result, tuple):
                result, graph = result
                size_policy = pyqt6_qtwidgets.QSizePolicy(
                    pyqt6_qtwidgets.QSizePolicy.Policy.Expanding, pyqt6_qtwidgets.QSizePolicy.Policy.Expanding
                )
                graph.setSizePolicy(size_policy)

                self.layout_output_pictures.addWidget(graph)

                self.delete_image()
                self.picture_obj = graph

        except ValidationError as e:
            result = self.__get_error_message(e.errors())
        except ValueError as e:
            result = str(e)
        except RecursionError:
            result = "Ошибка: Бесконечный цикл. Проверьте значение шага."
        self.text_entry.setText(str(result))

    def delete_image(self):
        if not self.picture_obj:
            return
        self.layout_input.removeWidget(self.picture_obj)
        self.picture_obj.deleteLater()
        self.picture_obj = None
