import configparser
import os

class ConfigReader:
    """
    ConfigReaderは設定ファイルを読み込むためのクラスです。

    Attributes:
        config_file (str): 設定ファイルのパス。
        config (configparser.ConfigParser): configparserオブジェクト。
    """

    def __init__(self, config_file):
        """
        ConfigReaderのコンストラクタ。

        Args:
            config_file (str): 設定ファイルのパス。
        """
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        # ファイルが存在するか確認します。
        if not os.path.exists(self.config_file):
            print(f"警告: 設定ファイル {self.config_file} が見つかりません。")
        else:
            self.config.read(self.config_file, 'UTF-8')

    # コンフィグを指定しない場合のInit関数
    # def __init__(self) -> None:
    #     # Config読み込み
    #     config = configparser.ConfigParser()
    #     config.read('./config.ini', 'UTF-8')

    def get(self, section, option):
        """
        指定したセクションとオプションの値を取得します。

        Args:
            section (str): セクション名。
            option (str): オプション名。

        Returns:
            str: 指定したセクションとオプションの値。
        """
        # check section
        if not self.config.has_section(section):
            print(f"警告: セクション {section} が見つかりません。")
            return None

        # check option
        if not self.config.has_option(section, option):
            print(f"警告: オプション {option} が見つかりません。")
            return None

        # get() => strで取得
        # その他データ型違い　getint(), getfloat(), getboolean()
        return self.config.get(section, option)

    def get_list(self, section, option):
        '''
        指定したセクションとオプションの値を取得します。

        Args:
            section (str): セクション名。
            option (str): オプション名。

        Returns:
            list(str): 指定したセクションとオプションの値。
        '''
        # check section
        if not self.config.has_section(section):
            print(f"警告: セクション {section} が見つかりません。")
            return None

        # check option
        if not self.config.has_option(section, option):
            print(f"警告: オプション {option} が見つかりません。")
            return None

        # 以下の処理では、"[xx, yy]"が戻り値になるため、astを使用してリストとして返す
        # return self.config.get(section, option)
        return ast.literal_eval(self.config.get(section, option))


# test
if __name__ == "__main__":
    # ConfigReaderクラスのインスタンスを作成します。
    config_reader = ConfigReader('config.ini')

    # 'section_name'セクションの'option_name'オプションの値を取得します。
    value = config_reader.get('tool', 'var')
    print(value)
    value_l = config_reader.get_list('tool', 'var')
    print(value_l)

    # 例外パターン
    value_e = config_reader.get('ool', 'var')
    print(value_e)

    value_e = config_reader.get('tool', 'ar')
    print(value_e)

    # ConfigReaderクラスのインスタンスを作成します。
    config_reader_e = ConfigReader('XXconfig.ini')
    value_e = config_reader_e.get('cpytool', 'target_fsm_header_range')


