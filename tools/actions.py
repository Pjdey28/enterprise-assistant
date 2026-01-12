# Mock enterprise actions (NO real execution)

ACTION_SCHEMAS = [
    {
        "name": "create_it_ticket",
        "description": "Create an IT service desk ticket",
        "parameters": {
            "type": "object",
            "properties": {
                "issue_type": {"type": "string"},
                "priority": {"type": "string"},
                "description": {"type": "string"}
            },
            "required": ["issue_type", "priority", "description"]
        }
    },
    {
        "name": "schedule_meeting",
        "description": "Schedule a meeting with a department",
        "parameters": {
            "type": "object",
            "properties": {
                "department": {"type": "string"},
                "purpose": {"type": "string"},
                "preferred_date": {"type": "string"}
            },
            "required": ["department", "purpose"]
        }
    },
    {
        "name": "request_leave",
        "description": "Submit a leave request",
        "parameters": {
            "type": "object",
            "properties": {
                "leave_type": {"type": "string"},
                "start_date": {"type": "string"},
                "end_date": {"type": "string"},
                "reason": {"type": "string"}
            },
            "required": ["leave_type", "start_date", "end_date"]
        }
    }
]
