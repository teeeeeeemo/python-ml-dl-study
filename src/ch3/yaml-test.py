import yaml

yaml_str = """
Date: 2017-08-08
ChampionList:
- champion_id: 1000
  name: Teemo
  position: top
  skill: ap
- champion_id: 1001
  name: Vayne
  position: bottom
  skill: ad
- champion_id: 1002
  name: Ahri
  position: mid
  skill: ap
"""

data = yaml.load(yaml_str)

for champion in data['ChampionList']:
	print(champion["name"], champion["skill"])
