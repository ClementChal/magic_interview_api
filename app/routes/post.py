from flask import request, Blueprint
from app.db import get_supabase

bp = Blueprint("posts", __name__, url_prefix="/post")


@bp.route("", methods=["GET"])
def get_posts():
    try:
        supabase = get_supabase()
        response = supabase.table("linkedin_post").select("*").execute()
        return response.data
    except Exception as e:
        return {"error": str(e)}, 500


@bp.route("", methods=["POST"])
def create_post():
    try:
        supabase = get_supabase()
        data = request.get_json()
        response = supabase.table("linkedin_post").insert(data).execute()
        return response.data[0], 201
    except Exception as e:
        return {"error": str(e)}, 500


@bp.route("/<pk>", methods=["PATCH"])
def patch_post(pk):
    try:
        supabase = get_supabase()
        data = request.get_json()
        existing_post = (
            supabase.table("linkedin_post").select("id").eq("id", pk).single().execute()
        )

        if not existing_post.data:
            return {"error": "Post non trouvé"}, 404

        response = supabase.table("linkedin_post").update(data).eq("id", pk).execute()

        return response.data[0]

    except Exception as e:
        return {"error": str(e)}, 500


@bp.route("/<pk>", methods=["DELETE"])
def delete_post(pk: str):
    try:
        supabase = get_supabase()
        response = supabase.table("linkedin_post").delete().eq("id", pk).execute()

        if not response.data:
            return {"error": "Post Linkedin non trouvé"}, 404

        return {"message": f"Post Linkedin {pk} supprimé avec succès"}, 200

    except Exception as e:
        return {"error": str(e)}, 500
