ADMIN_PERMISSIONS = (
	(1, "Super Admin"),
)

ADMIN_ROLE = (
	(1, "Super Admin"),
	(2, "Admin"),
)

ORGANISATION_STATUS = (
	(1, "Active"),
	(2, "Inactive"),
	(3, "Awaiting Approval"),
	(4, "Draft"), # Draft
)

VOLUNTEER_STATUS = (
	(1, "Active"),
	(2, "DeActivated"),
	(3, "Review"),
)

VOLUNTEER_COLOR = (
	(0, "NiL"),
	(1, "Green"),
	(2, "Orange"),
	(3, "Red"),
)

GENDER = (
	(1, "Male"),
	(2, "Female"),
	(3, "Other"),
	(4, "Not to Answer"),
)

ROLE_STATUS = (
	(1, "Active"),
	(2, "DeActivated"),
	(3, "On-Hold")
)

COMMENT_CATEGORY = (
	(1, "Organisation"),
	(2, "Volunteer"),
	(3, "Role"),
)