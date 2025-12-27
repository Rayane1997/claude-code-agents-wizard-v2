from sqlalchemy.orm import Session
from sqlalchemy import desc, asc
from typing import Optional, List
from urllib.parse import urlparse
from ..models.product import Product, ProductStatus
from ..schemas.product import ProductCreate, ProductUpdate

def extract_domain(url: str) -> str:
    """Extract domain from URL"""
    parsed = urlparse(url)
    domain = parsed.netloc or parsed.path
    # Remove www. prefix
    if domain.startswith('www.'):
        domain = domain[4:]
    return domain.lower()

def get_products(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    status: Optional[ProductStatus] = None,
    domain: Optional[str] = None,
    sort_by: str = "created_at",
    sort_order: str = "desc",
) -> tuple[List[Product], int]:
    """Get products with filtering and pagination"""
    query = db.query(Product)

    # Filters
    if status:
        query = query.filter(Product.status == status)
    if domain:
        query = query.filter(Product.domain == domain)

    # Count total
    total = query.count()

    # Sorting
    order_column = getattr(Product, sort_by, Product.created_at)
    if sort_order == "asc":
        query = query.order_by(asc(order_column))
    else:
        query = query.order_by(desc(order_column))

    # Pagination
    products = query.offset(skip).limit(limit).all()

    return products, total

def get_product(db: Session, product_id: int) -> Optional[Product]:
    """Get single product by ID"""
    return db.query(Product).filter(Product.id == product_id).first()

def create_product(db: Session, product: ProductCreate) -> Product:
    """Create new product"""
    # Extract domain from URL
    domain = extract_domain(product.url)

    db_product = Product(
        name=product.name,
        url=product.url,
        domain=domain,
        target_price=product.target_price,
        image_url=product.image_url,
        check_frequency_hours=product.check_frequency_hours,
        tags=product.tags,
        notes=product.notes,
        status=ProductStatus.ACTIVE,
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product_update: ProductUpdate) -> Optional[Product]:
    """Update existing product"""
    db_product = get_product(db, product_id)
    if not db_product:
        return None

    # Update only provided fields
    update_data = product_update.model_dump(exclude_unset=True)

    # If URL is updated, re-extract domain
    if "url" in update_data:
        update_data["domain"] = extract_domain(update_data["url"])

    for field, value in update_data.items():
        setattr(db_product, field, value)

    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int) -> bool:
    """Delete product (cascade deletes price_history and alerts)"""
    db_product = get_product(db, product_id)
    if not db_product:
        return False

    db.delete(db_product)
    db.commit()
    return True

def get_domains(db: Session) -> List[str]:
    """Get list of unique domains"""
    domains = db.query(Product.domain).distinct().all()
    return [d[0] for d in domains]
