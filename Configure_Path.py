import configparser
cnfg = configparser.ConfigParser()
cnfg.optionxform = str
cnfg['PATHS'] = {'DIR': r"C:\modeltech64_10.5\examples\SAC\Instructions",
        'PM_LOCATE': r"C:\modeltech64_10.5\examples\memory_files\pm_file.txt",
        'DM_LOCATE': r"C:\modeltech64_10.5\examples\memory_files\dm_file.txt",
        'DMrdfl_LOCATE': r"C:\modeltech64_10.5\examples\SAC\DMrd_files",
        'MEMfail_LOCATE': r"C:\modeltech64_10.5\examples\SAC\MEMfail_files"}
cnfg['IDENTIFIER'] = {'idntfr': "_"}
cnfg['AVOID'] = {'pm_file.txt': "",
        'dm_file.txt': ""}
with open('Path.ini', 'w') as pathfl:
    cnfg.write(pathfl)
