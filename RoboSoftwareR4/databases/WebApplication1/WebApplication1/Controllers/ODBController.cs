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
    public class ODBController : Controller
    {
        private RoboDbMainEntities db = new RoboDbMainEntities();

        // GET: ODB
        public ActionResult Index()
        {
            return View(db.ODBs.ToList());
        }

        // GET: ODB/Details/5
        public ActionResult Details(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            ODB oDB = db.ODBs.Find(id);
            if (oDB == null)
            {
                return HttpNotFound();
            }
            return View(oDB);
        }

        // GET: ODB/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: ODB/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "OrganName")] ODB oDB)
        {
            if (ModelState.IsValid)
            {
                oDB.Id = db.ODBs.Select(x => x.Id).Count();
                db.ODBs.Add(oDB);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            return View(oDB);
        }

        // GET: ODB/Edit/5
        public ActionResult Edit(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            ODB oDB = db.ODBs.Find(id);
            if (oDB == null)
            {
                return HttpNotFound();
            }
            return View(oDB);
        }

        // POST: ODB/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "Id,OrganName")] ODB oDB)
        {
            if (ModelState.IsValid)
            {
                db.Entry(oDB).State = System.Data.Entity.EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            return View(oDB);
        }

        // GET: ODB/Delete/5
        public ActionResult Delete(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            ODB oDB = db.ODBs.Find(id);
            if (oDB == null)
            {
                return HttpNotFound();
            }
            return View(oDB);
        }

        // POST: ODB/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            ODB oDB = db.ODBs.Find(id);
            db.ODBs.Remove(oDB);
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
