using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using WebApplication1.Models;

namespace WebApplication1.Controllers
{
    public class QdbsController : Controller
    {
        private RoboDbMainEntities db = new RoboDbMainEntities();

        // GET: Qdbs
        public ActionResult Index()
        {
            return View(db.Qdbs.ToList());
        }

        // GET: Qdbs/Details/5
        public ActionResult Details(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Qdb qdb = db.Qdbs.Find(id);
            if (qdb == null)
            {
                return HttpNotFound();
            }
            return View(qdb);
        }

        // GET: Qdbs/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: Qdbs/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "nameofsymp,answer,question,state,KindId")] Qdb qdb)
        {
            if (ModelState.IsValid)
            {
                qdb.SymptomId = db.Qdbs.Select(x => x.SymptomId).Count();
                db.Qdbs.Add(qdb);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            return View(qdb);
        }

        // GET: Qdbs/Edit/5
        public ActionResult Edit(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Qdb qdb = db.Qdbs.Find(id);
            if (qdb == null)
            {
                return HttpNotFound();
            }
            return View(qdb);
        }

        // POST: Qdbs/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "nameofsymp,answer,question,state,SymptomId,KindId")] Qdb qdb)
        {
            if (ModelState.IsValid)
            {
                db.Entry(qdb).State = System.Data.Entity.EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            return View(qdb);
        }

        // GET: Qdbs/Delete/5
        public ActionResult Delete(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Qdb qdb = db.Qdbs.Find(id);
            if (qdb == null)
            {
                return HttpNotFound();
            }
            return View(qdb);
        }

        // POST: Qdbs/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            Qdb qdb = db.Qdbs.Find(id);
            db.Qdbs.Remove(qdb);
            db.SaveChanges();
            return RedirectToAction("Index");
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                db.Dispose();
            }
            base.Dispose(disposing);
        }
    }
}
