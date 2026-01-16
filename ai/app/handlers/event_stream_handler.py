# //app/routes/sse_routes.py
from flask import Blueprint, Response, session
from app.utils import create_event_stream

sse_bp = Blueprint('sse', __name__)

@sse_bp.route('/events')
def events():
    """SSE事件流端点"""
    user_id = session.get('user_id')
    if not user_id:
        return Response(
            "data: {\"type\": \"error\", \"message\": \"Invalid session\"}\n\n",
            mimetype='text/event-stream'
        )

    return Response(
        create_event_stream(user_id),
        mimetype='text/event-stream',
        headers={
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Access-Control-Allow-Origin': '*',
            'X-Accel-Buffering': 'no'
        }
    )
