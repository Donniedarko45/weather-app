from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, FeedbackModel
from app.models import Feedback

router = APIRouter(
    prefix="/feedback",
    tags=["Feedback"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_feedback(feedback: Feedback, db: Session = Depends(get_db)):
    db_feedback = FeedbackModel(**feedback.dict())
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return {"feedback_id": db_feedback.id, "feedback": feedback}

@router.get("/")
def get_all_feedback(db: Session = Depends(get_db)):
    return db.query(FeedbackModel).all()

@router.get("/{feedback_id}")
def get_feedback(feedback_id: int, db: Session = Depends(get_db)):
    feedback = db.query(FeedbackModel).filter(FeedbackModel.id == feedback_id).first()
    if feedback is None:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return feedback

@router.put("/{feedback_id}")
def update_feedback(feedback_id: int, feedback: Feedback, db: Session = Depends(get_db)):
    db_feedback = db.query(FeedbackModel).filter(FeedbackModel.id == feedback_id).first()
    if db_feedback is None:
        raise HTTPException(status_code=404, detail="Feedback not found")
    for key, value in feedback.dict().items():
        setattr(db_feedback, key, value)
    db.commit()
    db.refresh(db_feedback)
    return {"message": "Feedback updated", "feedback": feedback}

@router.delete("/{feedback_id}")
def delete_feedback(feedback_id: int, db: Session = Depends(get_db)):
    db_feedback = db.query(FeedbackModel).filter(FeedbackModel.id == feedback_id).first()
    if db_feedback is None:
        raise HTTPException(status_code=404, detail="Feedback not found")
    db.delete(db_feedback)
    db.commit()
    return {"message": "Feedback deleted"}
