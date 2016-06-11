
Basic_Stats_Desc = {
	'Strength': """Strength is the measure of the power you are capable of generating.
This has an effect on the amount of damage that you are capable of causing, and the weapons you can use.""",
	'Stamina': """Stamina is a measure of how long you can work.  It has an effect on
how long you can travel without getting tired.""",
	'Dexterity': """Dexterity is the measure of you hand eye coordination.  It has an effect
on your ability to evade attacks, as well as how likely you are to land good hits.""",
}

Magic_Desc = {
	'Fire': "Utilize the power of the flame to incinerate your foes.",
	'Ice': "Utilize the power of the frost to cause severe damage to foes.",
	'Water': "Utilize the power of the seas to drown your foes.",
	'Thunder': "Utilize the power of the storms to electrocute your foes.",
	'Air': "Utilize the power of the skies to damage your foes.",
	'Earth': "Utilize the power of  the earth cause severe damage to foes.",
}

Special_Skills_Desc = {
	'Medical': {

	}
}

Magic_Level_Reqs = {

}

Magic_Damage_Key = {

}

Special_Skills_Values = {

}

items_usage = {
	potion: {
		value: 50,
		description: """
		Potions are used when you find yourself in dire straits.\n
		They return your vitality, and heal wounds that are superficial.\n
		Heals 5 health.
		""",
		effect: def potion(self):
		self.health = self.health + 5,
	}
}
